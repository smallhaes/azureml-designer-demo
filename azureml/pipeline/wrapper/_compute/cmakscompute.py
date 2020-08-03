# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Contains functionality for managing Azure Machine Learning compute targets in Azure Machine Learning."""

import copy
import json
import requests
from azureml._compute._constants import MLC_COMPUTE_RESOURCE_ID_FMT
from azureml._compute._constants import MLC_WORKSPACE_API_VERSION
from azureml.core.compute import ComputeTarget
from azureml.core.compute.compute import ComputeTargetAttachConfiguration
from azureml.exceptions import ComputeTargetException
from ._util import cmakscompute_payload_template


class CmAksCompute(ComputeTarget):
    """CmAksCompute is a customer managed AKS infrastructure, which can be attached to workspace
    by cluster admin. User granted access and quota to the compute can easily specify and submit a one-node or
    distributed multi-node training job to the compute. The compute executes in a containerized environment and
    packages your model dependencies in a docker container.
    For more information, see `What are compute targets in Azure Machine
    Learning? <https://docs.microsoft.com/azure/machine-learning/concept-compute-target>`_

    .. remarks::

        In the following example, a persistent compute target provisioned by
        :class:`azureml.contrib.core.compute.cmakscompute.CmAksCompute` is created. The ``provisioning_configuration``
        parameter in this example is of type
        :class:`azureml.contrib.core.compute.cmakscompute.CmAksComputeAttachConfiguration`,
         which is a child class of :class:`azureml.contrib.core.compute.cmakscompute.ComputeTargetAttachConfiguration`.

    :param workspace: The workspace object containing the CmAksCompute object to retrieve.
    :type workspace: azureml.core.Workspace
    :param name: The name of the of the Compute object to retrieve.
    :type name: str
    """

    _compute_type = 'CmAks'
    vm_size = 1

    def _initialize(self, workspace, obj_dict):
        """Initialize implementation method.

        :param workspace:
        :type workspace: azureml.core.Workspace
        :param obj_dict:
        :type obj_dict: dict
        :return:
        :rtype: None
        """
        name = obj_dict['name']
        compute_resource_id = MLC_COMPUTE_RESOURCE_ID_FMT.format(workspace.subscription_id, workspace.resource_group,
                                                                 workspace.name, name)
        resource_manager_endpoint = self._get_resource_manager_endpoint(
            workspace)
        mlc_endpoint = '{}{}'.format(
            resource_manager_endpoint, compute_resource_id)
        location = obj_dict['location']
        compute_type = obj_dict['properties']['computeType']
        tags = obj_dict['tags']
        description = obj_dict['properties']['description']
        created_on = obj_dict['properties'].get('createdOn')
        modified_on = obj_dict['properties'].get('modifiedOn')
        cluster_resource_id = obj_dict['properties']['resourceId']
        cluster_location = obj_dict['properties']['computeLocation'] \
            if 'computeLocation' in obj_dict['properties'] else None
        provisioning_state = obj_dict['properties']['provisioningState']
        provisioning_errors = obj_dict['properties']['provisioningErrors']
        is_attached = obj_dict['properties']['isAttachedCompute'] \
            if 'isAttachedCompute' in obj_dict['properties'] else None
        node_pool = obj_dict['properties']['properties']['nodePool'] \
            if obj_dict['properties']['properties'] else None
        nodes_count = obj_dict['properties']['properties']['nodesCount'] \
            if obj_dict['properties']['properties'] else None
        public_ip = obj_dict['properties']['properties']['publicIp'] \
            if obj_dict['properties']['properties'] else None
        cluster_fqdn = obj_dict['properties']['properties']['clusterFqdn'] \
            if obj_dict['properties']['properties'] else None

        super(CmAksCompute, self)._initialize(compute_resource_id, name, location, compute_type, tags, description,
                                              created_on, modified_on, provisioning_state, provisioning_errors,
                                              cluster_resource_id, cluster_location, workspace, mlc_endpoint, None,
                                              workspace._auth, is_attached)
        self.node_pool = node_pool
        self.nodes_count = nodes_count
        self.public_ip = public_ip
        self.cluster_fqdn = cluster_fqdn

    def __repr__(self):
        """Return the string representation of the CmAksCompute object.

        :return: String representation of the CmAksCompute object
        :rtype: str
        """
        return super().__repr__()

    @staticmethod
    def _attach(workspace, name, config):
        """Associate an existing cmaks compute resource with the provided workspace.

        :param workspace: The workspace object to associate the compute resource with.
        :type workspace: azureml.core.Workspace
        :param name: The name to associate with the compute resource inside the provided workspace. Does not have to
            match the name of the compute resource to be attached..
        :type name: str
        :param config: Attach configuration object.
        :type config: azureml.contrib.core.compute.cmakscompute.CmAksComputeAttachConfiguration
        :return: A CmAksCompute object representation of the compute object.
        :rtype: azureml.contrib.core.compute.cmakscompute.CmAksCompute
        :raises: :class:`azureml.exceptions.ComputeTargetException`
        """
        attach_payload = CmAksCompute._build_attach_payload(config, workspace)
        return ComputeTarget._attach(workspace, name, attach_payload, CmAksCompute)

    @staticmethod
    def attach_configuration(node_pool=None, nodes_count=-1, resource_group=None, cluster_name=None,
                             resource_id=None, description=' '):
        """Create a configuration object for attaching an cmaks compute target.

        :param node_pool: The node pool of AKS cluster.
        :type node_pool: str
        :param nodes_count: The maximum node count can be used by a job
        :type nodes_count: int
        :param resource_id: The resource id.
        :type resource_id: str
        :param description: The description of cmaks compute target.
        :type description: str
        :return: A configuration object to be used when attaching a Compute object.
        :rtype: azureml.contrib.core.compute.cmakscompute.CmAksComputeAttachConfiguration
        """
        config = CmAksComputeAttachConfiguration(
            node_pool, nodes_count, resource_group, cluster_name, resource_id, description)
        return config

    @staticmethod
    def _build_attach_payload(config, workspace):
        """Build attach payload.

        :param config: the cmaks compute configuration.
        :type config: azureml.contrib.core.compute.cmakscompute.CmAksComputeAttachConfiguration
        :param location:
        :type location: str
        :return:
        :rtype: dict
        """
        json_payload = copy.deepcopy(cmakscompute_payload_template)
        del (json_payload['properties']['computeLocation'])

        if not config:
            raise ComputeTargetException('Error, missing config.')

        if not config.node_pool:
            raise ComputeTargetException('Error, missing node_pool.')

        if not config.nodes_count:
            raise ComputeTargetException('Error, missing nodes_count')

        attach_resource_id = None
        if config.resource_id:
            attach_resource_id = config.resource_id
        elif config.resource_group and config.cluster_name:
            attach_resource_id = CmAksCompute._build_aks_resource_id(
                workspace.subscription_id, config.resource_group, config.cluster_name)

        if not attach_resource_id:
            raise ComputeTargetException(
                'Error, missing resource_id and resource group and cluster name.')

        if not config.description:
            raise ComputeTargetException('Error, missing description.')

        json_payload['properties']['properties']['nodePool'] = config.node_pool
        json_payload['properties']['properties']['nodesCount'] = config.nodes_count
        json_payload['properties']['resourceId'] = attach_resource_id
        json_payload['properties']['description'] = config.description
        return json_payload

    @staticmethod
    def _build_aks_resource_id(subscription_id, resource_group, cluster_name):
        """Build the Azure resource ID for the compute resource.

        :param subscription_id: The Azure subscription ID
        :type subscription_id: str
        :param resource_group: Name of the resource group in which the AKS is located.
        :type resource_group: str
        :param cluster_name: The AKS cluster name
        :type cluster_name: str
        :return: The Azure resource ID for the compute resource
        :rtype: str
        """
        AKS_RESOURCE_ID_FMT = ('/subscriptions/{}/resourcegroups/{}/providers/Microsoft.ContainerService/'
                               'managedClusters/{}')
        return AKS_RESOURCE_ID_FMT.format(subscription_id, resource_group, cluster_name)

    def refresh_state(self):
        """Perform an in-place update of the properties of the object.

        This method updates the properties based on the current state of the corresponding cloud object.
        This is primarily used for manual polling of compute state.
        """
        cluster = CmAksCompute(self.workspace, self.name)
        self.modified_on = cluster.modified_on
        self.provisioning_state = cluster.provisioning_state
        self.provisioning_errors = cluster.provisioning_errors
        self.cluster_resource_id = cluster.cluster_resource_id
        self.cluster_location = cluster.cluster_location
        self.node_pool = cluster.node_pool
        self.nodes_count = cluster.nodes_count
        self.public_ip = cluster.public_ip
        self.cluster_fqdn = cluster.cluster_fqdn

    def delete(self):
        """Delete is not supported for an CmAksCompute object. Use :meth:`detach` instead.

        :raises: :class:`azureml.exceptions.ComputeTargetException`
        """
        raise ComputeTargetException(
            'Delete is not supported for CmAksCompute object. Try to use detach instead.')

    def detach(self):
        """Detach the CmAksCompute object from its associated workspace.

        Underlying cloud objects are not deleted, only the association is removed.

        :raises: :class:`azureml.exceptions.ComputeTargetException`
        """
        self._delete_or_detach('detach')

    def get_credentials(self):
        """Retrieve the credentials(AdminKubeConfig) for the cmaks target.

        :return: Credentials for the cmaks target
        :rtype: dict
        :raises: ComputeTargetException
        """
        endpoint = self._mlc_endpoint + '/listKeys'
        headers = self._auth.get_authentication_header()
        params = {'api-version': MLC_WORKSPACE_API_VERSION}
        resp = requests.post(endpoint, params=params, headers=headers)

        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError:
            raise ComputeTargetException('Received bad response from MLC:\n'
                                         'Response Code: {}\n'
                                         'Headers: {}\n'
                                         'Content: {}'.format(resp.status_code, resp.headers, resp.content))
        content = resp.content
        if isinstance(content, bytes):
            content = content.decode('utf-8')
        creds_content = json.loads(content)
        return creds_content

    def serialize(self):
        """Convert this CmAksCompute object into a JSON serialized dictionary.

        :return: The JSON representation of this CmAksCompute object.
        :rtype: dict
        """
        CmAksCompute_properties = {'nodePool': self.node_pool,
                                   'nodesCount': self.nodes_count,
                                   'publicIp': self.public_ip,
                                   'clusterFqdn': self.cluster_fqdn}
        cluster_properties = {'computeType': self.type, 'computeLocation': self.cluster_location,
                              'description': self.description, 'resourceId': self.cluster_resource_id,
                              'provisioningErrors': self.provisioning_errors,
                              'provisioningState': self.provisioning_state, 'properties': CmAksCompute_properties}
        return {'id': self.id, 'name': self.name, 'tags': self.tags, 'location': self.location,
                'properties': cluster_properties}

    @staticmethod
    def deserialize(workspace, object_dict):
        """Convert a JSON object into a CmAksCompute object.

        .. remarks::

            Raises a :class:`azureml.exceptions.ComputeTargetException` if the provided
            workspace is not the workspace the Compute is associated with.

        :param workspace: The workspace object the CmAksCompute object is associated with.
        :type workspace: azureml.core.Workspace
        :param object_dict: A JSON object to convert to a CmAksCompute object.
        :type object_dict: dict
        :return: The CmAksCompute representation of the provided JSON object.
        :rtype: azureml.contrib.core.compute.cmakscompute.CmAksCompute
        :raises: :class:`azureml.exceptions.ComputeTargetException`
        """
        CmAksCompute._validate_get_payload(object_dict)
        target = CmAksCompute(None, None)
        target._initialize(workspace, object_dict)
        return target

    @staticmethod
    def _validate_get_payload(payload):
        if 'properties' not in payload or 'computeType' not in payload['properties']:
            raise ComputeTargetException('Invalid cluster payload:\n'
                                         '{}'.format(payload))
        if payload['properties']['computeType'] != CmAksCompute._compute_type:
            raise ComputeTargetException('Invalid cluster payload, not "{}":\n'
                                         '{}'.format(CmAksCompute._compute_type, payload))
        for arm_key in ['location', 'id', 'tags']:
            if arm_key not in payload:
                raise ComputeTargetException('Invalid cluster payload, missing ["{}"]:\n'
                                             '{}'.format(arm_key, payload))
        for key in ['properties', 'provisioningErrors', 'description', 'provisioningState', 'resourceId']:
            if key not in payload['properties']:
                raise ComputeTargetException('Invalid cluster payload, missing ["properties"]["{}"]:\n'
                                             '{}'.format(key, payload))


class CmAksComputeAttachConfiguration(ComputeTargetAttachConfiguration):
    """Represents configuration parameters for attaching cmaks compute targets.

    Use the ``attach_configuration`` method of the
    :class:`azureml.contrib.core.compute.cmakscompute.CmAksCompute` class to
    specify attach parameters.

    :param node_pool: The node pool of AKS cluster for the compute resource being attached.
    :type node_pool: str
    :param nodes_count: The maximum node count used per job
    :type nodes_count: int
    :param resource_id: The Azure resource Id for the compute resource being attached.
    :type resource_id: str
    :param description: The description of compute target.
    :type description: str
    :return: The configuration object
    :rtype: azureml.contrib.core.compute.cmakscompute.CmAksComputeAttachConfiguration
    """

    def __init__(self, node_pool, nodes_count, resource_group, cluster_name, resource_id, description=''):
        """Initialize the configuration object.

        :param node_pool: The node pool of AKS cluster for the compute resource being attached.
        :type node_pool: str
        :param nodes_count: The maximum node count used per job
        :type nodes_count: int
        :param resource_id: The Azure resource Id for the compute resource being attached.
        :type resource_id: str
        :param description: The description of compute target.
        :type description: str
        :return: The configuration object
        :rtype: azureml.contrib.core.compute.cmakscompute.CmAksComputeAttachConfiguration
        """
        super(CmAksComputeAttachConfiguration, self).__init__(CmAksCompute)
        self.node_pool = node_pool
        self.nodes_count = nodes_count
        self.resource_group = resource_group
        self.cluster_name = cluster_name
        self.resource_id = resource_id
        self.description = description
        self.validate_configuration()

    def validate_configuration(self):
        """Check that the specified configuration values are valid.

        Raises a :class:`azureml.exceptions.ComputeTargetException` if validation fails.

        :raises: :class:`azureml.exceptions.ComputeTargetException`
        """
        if not self.node_pool:
            raise ComputeTargetException('node pool is not provided.')

        if self.nodes_count is None:
            raise ComputeTargetException('nodes count is not provided.')

        if self.description is None:
            raise ComputeTargetException('description string is not provided.')

        if self.resource_id:
            # resource_id is provided, validate resource_id
            resource_parts = self.resource_id.split('/')
            if len(resource_parts) != 9:
                raise ComputeTargetException(
                    'Invalid resource_id provided: {}'.format(self.resource_id))
            resource_type = resource_parts[6]
            if resource_type != 'Microsoft.ContainerService':
                raise ComputeTargetException('Invalid resource_id provided, resource type {} does not match for '
                                             'Microsoft.ContainerService'.format(resource_type))
        elif not (self.cluster_name and self.resource_group):
            # neither resource_id nor other info is provided.
            raise ComputeTargetException('Please provide resource_id or resource group and cluster '
                                         'for the cmaks Compute compute resource being attached.')
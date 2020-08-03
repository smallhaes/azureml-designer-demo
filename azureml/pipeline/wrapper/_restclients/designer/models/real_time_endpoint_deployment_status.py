# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .aks_replica_status import AKSReplicaStatus


class RealTimeEndpointDeploymentStatus(AKSReplicaStatus):
    """RealTimeEndpointDeploymentStatus.

    :param desired_replicas:
    :type desired_replicas: int
    :param updated_replicas:
    :type updated_replicas: int
    :param available_replicas:
    :type available_replicas: int
    :param error:
    :type error: ~designer.models.AKSReplicaStatusError
    """

    _attribute_map = {
        'desired_replicas': {'key': 'desiredReplicas', 'type': 'int'},
        'updated_replicas': {'key': 'updatedReplicas', 'type': 'int'},
        'available_replicas': {'key': 'availableReplicas', 'type': 'int'},
        'error': {'key': 'error', 'type': 'AKSReplicaStatusError'},
    }

    def __init__(self, **kwargs):
        super(RealTimeEndpointDeploymentStatus, self).__init__(**kwargs)
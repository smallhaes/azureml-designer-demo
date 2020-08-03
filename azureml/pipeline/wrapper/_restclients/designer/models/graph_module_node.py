# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GraphModuleNode(Model):
    """GraphModuleNode.

    :param id:
    :type id: str
    :param module_id:
    :type module_id: str
    :param module_type: Possible values include: 'None', 'BatchInferencing'
    :type module_type: str or ~designer.models.ModuleType
    :param comment:
    :type comment: str
    :param module_parameters:
    :type module_parameters: list[~designer.models.ParameterAssignment]
    :param module_metadata_parameters:
    :type module_metadata_parameters:
     list[~designer.models.ParameterAssignment]
    :param module_output_settings:
    :type module_output_settings: list[~designer.models.OutputSetting]
    :param module_input_settings:
    :type module_input_settings: list[~designer.models.InputSetting]
    :param use_graph_default_compute:
    :type use_graph_default_compute: bool
    :param use_graph_default_datastore:
    :type use_graph_default_datastore: bool
    :param runconfig:
    :type runconfig: str
    :param cloud_settings:
    :type cloud_settings: ~designer.models.GraphModuleNodeCloudSettings
    :param regenerate_output:
    :type regenerate_output: bool
    :param control_inputs:
    :type control_inputs: list[~designer.models.ControlInput]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'module_id': {'key': 'moduleId', 'type': 'str'},
        'module_type': {'key': 'moduleType', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'module_parameters': {'key': 'moduleParameters', 'type': '[ParameterAssignment]'},
        'module_metadata_parameters': {'key': 'moduleMetadataParameters', 'type': '[ParameterAssignment]'},
        'module_output_settings': {'key': 'moduleOutputSettings', 'type': '[OutputSetting]'},
        'module_input_settings': {'key': 'moduleInputSettings', 'type': '[InputSetting]'},
        'use_graph_default_compute': {'key': 'useGraphDefaultCompute', 'type': 'bool'},
        'use_graph_default_datastore': {'key': 'useGraphDefaultDatastore', 'type': 'bool'},
        'runconfig': {'key': 'runconfig', 'type': 'str'},
        'cloud_settings': {'key': 'cloudSettings', 'type': 'GraphModuleNodeCloudSettings'},
        'regenerate_output': {'key': 'regenerateOutput', 'type': 'bool'},
        'control_inputs': {'key': 'controlInputs', 'type': '[ControlInput]'},
    }

    def __init__(self, **kwargs):
        super(GraphModuleNode, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.module_id = kwargs.get('module_id', None)
        self.module_type = kwargs.get('module_type', None)
        self.comment = kwargs.get('comment', None)
        self.module_parameters = kwargs.get('module_parameters', None)
        self.module_metadata_parameters = kwargs.get('module_metadata_parameters', None)
        self.module_output_settings = kwargs.get('module_output_settings', None)
        self.module_input_settings = kwargs.get('module_input_settings', None)
        self.use_graph_default_compute = kwargs.get('use_graph_default_compute', None)
        self.use_graph_default_datastore = kwargs.get('use_graph_default_datastore', None)
        self.runconfig = kwargs.get('runconfig', None)
        self.cloud_settings = kwargs.get('cloud_settings', None)
        self.regenerate_output = kwargs.get('regenerate_output', None)
        self.control_inputs = kwargs.get('control_inputs', None)
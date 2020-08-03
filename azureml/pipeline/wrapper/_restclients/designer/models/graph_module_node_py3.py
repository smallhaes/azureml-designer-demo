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

    def __init__(self, *, id: str=None, module_id: str=None, module_type=None, comment: str=None, module_parameters=None, module_metadata_parameters=None, module_output_settings=None, module_input_settings=None, use_graph_default_compute: bool=None, use_graph_default_datastore: bool=None, runconfig: str=None, cloud_settings=None, regenerate_output: bool=None, control_inputs=None, **kwargs) -> None:
        super(GraphModuleNode, self).__init__(**kwargs)
        self.id = id
        self.module_id = module_id
        self.module_type = module_type
        self.comment = comment
        self.module_parameters = module_parameters
        self.module_metadata_parameters = module_metadata_parameters
        self.module_output_settings = module_output_settings
        self.module_input_settings = module_input_settings
        self.use_graph_default_compute = use_graph_default_compute
        self.use_graph_default_datastore = use_graph_default_datastore
        self.runconfig = runconfig
        self.cloud_settings = cloud_settings
        self.regenerate_output = regenerate_output
        self.control_inputs = control_inputs
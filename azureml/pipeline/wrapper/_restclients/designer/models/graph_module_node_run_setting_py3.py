# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GraphModuleNodeRunSetting(Model):
    """GraphModuleNodeRunSetting.

    :param node_id:
    :type node_id: str
    :param module_id:
    :type module_id: str
    :param step_type:
    :type step_type: str
    :param run_settings:
    :type run_settings: list[~designer.models.RunSettingParameterAssignment]
    """

    _attribute_map = {
        'node_id': {'key': 'nodeId', 'type': 'str'},
        'module_id': {'key': 'moduleId', 'type': 'str'},
        'step_type': {'key': 'stepType', 'type': 'str'},
        'run_settings': {'key': 'runSettings', 'type': '[RunSettingParameterAssignment]'},
    }

    def __init__(self, *, node_id: str=None, module_id: str=None, step_type: str=None, run_settings=None, **kwargs) -> None:
        super(GraphModuleNodeRunSetting, self).__init__(**kwargs)
        self.node_id = node_id
        self.module_id = module_id
        self.step_type = step_type
        self.run_settings = run_settings
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UIComputeSelection(Model):
    """UIComputeSelection.

    :param compute_types:
    :type compute_types: list[str]
    :param require_gpu:
    :type require_gpu: bool
    :param os_types:
    :type os_types: list[str]
    :param compute_run_settings_mapping:
    :type compute_run_settings_mapping: dict[str,
     list[~designer.models.ComputeRunSettingParameter]]
    """

    _attribute_map = {
        'compute_types': {'key': 'computeTypes', 'type': '[str]'},
        'require_gpu': {'key': 'requireGpu', 'type': 'bool'},
        'os_types': {'key': 'osTypes', 'type': '[str]'},
        'compute_run_settings_mapping': {'key': 'computeRunSettingsMapping', 'type': '{[ComputeRunSettingParameter]}'},
    }

    def __init__(self, **kwargs):
        super(UIComputeSelection, self).__init__(**kwargs)
        self.compute_types = kwargs.get('compute_types', None)
        self.require_gpu = kwargs.get('require_gpu', None)
        self.os_types = kwargs.get('os_types', None)
        self.compute_run_settings_mapping = kwargs.get('compute_run_settings_mapping', None)
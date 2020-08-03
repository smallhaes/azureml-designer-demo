# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .mlc_compute_info_py3 import MlcComputeInfo


class ComputeSettingMlcComputeInfo(MlcComputeInfo):
    """ComputeSettingMlcComputeInfo.

    :param mlc_compute_type:
    :type mlc_compute_type: str
    """

    _attribute_map = {
        'mlc_compute_type': {'key': 'mlcComputeType', 'type': 'str'},
    }

    def __init__(self, *, mlc_compute_type: str=None, **kwargs) -> None:
        super(ComputeSettingMlcComputeInfo, self).__init__(mlc_compute_type=mlc_compute_type, **kwargs)
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MlcComputeInfo(Model):
    """MlcComputeInfo.

    :param mlc_compute_type:
    :type mlc_compute_type: str
    """

    _attribute_map = {
        'mlc_compute_type': {'key': 'mlcComputeType', 'type': 'str'},
    }

    def __init__(self, *, mlc_compute_type: str=None, **kwargs) -> None:
        super(MlcComputeInfo, self).__init__(**kwargs)
        self.mlc_compute_type = mlc_compute_type
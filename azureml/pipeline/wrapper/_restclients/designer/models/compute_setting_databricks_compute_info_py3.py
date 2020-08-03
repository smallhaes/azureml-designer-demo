# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .databricks_compute_info_py3 import DatabricksComputeInfo


class ComputeSettingDatabricksComputeInfo(DatabricksComputeInfo):
    """ComputeSettingDatabricksComputeInfo.

    :param existing_cluster_id:
    :type existing_cluster_id: str
    """

    _attribute_map = {
        'existing_cluster_id': {'key': 'existingClusterId', 'type': 'str'},
    }

    def __init__(self, *, existing_cluster_id: str=None, **kwargs) -> None:
        super(ComputeSettingDatabricksComputeInfo, self).__init__(existing_cluster_id=existing_cluster_id, **kwargs)
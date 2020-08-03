# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .data_path import DataPath


class DataSetDefinitionValueLiteralValue(DataPath):
    """DataSetDefinitionValueLiteralValue.

    :param data_store_name:
    :type data_store_name: str
    :param relative_path:
    :type relative_path: str
    :param sql_data_path:
    :type sql_data_path: ~designer.models.DataPathSqlDataPath
    """

    _attribute_map = {
        'data_store_name': {'key': 'dataStoreName', 'type': 'str'},
        'relative_path': {'key': 'relativePath', 'type': 'str'},
        'sql_data_path': {'key': 'sqlDataPath', 'type': 'DataPathSqlDataPath'},
    }

    def __init__(self, **kwargs):
        super(DataSetDefinitionValueLiteralValue, self).__init__(**kwargs)
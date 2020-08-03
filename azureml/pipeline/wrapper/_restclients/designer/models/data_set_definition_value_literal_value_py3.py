# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .data_path_py3 import DataPath


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

    def __init__(self, *, data_store_name: str=None, relative_path: str=None, sql_data_path=None, **kwargs) -> None:
        super(DataSetDefinitionValueLiteralValue, self).__init__(data_store_name=data_store_name, relative_path=relative_path, sql_data_path=sql_data_path, **kwargs)
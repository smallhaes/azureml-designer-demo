# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sql_data_path_py3 import SqlDataPath


class DataPathSqlDataPath(SqlDataPath):
    """DataPathSqlDataPath.

    :param sql_table_name:
    :type sql_table_name: str
    :param sql_query:
    :type sql_query: str
    :param sql_stored_procedure_name:
    :type sql_stored_procedure_name: str
    :param sql_stored_procedure_params:
    :type sql_stored_procedure_params:
     list[~designer.models.StoredProcedureParameter]
    """

    _attribute_map = {
        'sql_table_name': {'key': 'sqlTableName', 'type': 'str'},
        'sql_query': {'key': 'sqlQuery', 'type': 'str'},
        'sql_stored_procedure_name': {'key': 'sqlStoredProcedureName', 'type': 'str'},
        'sql_stored_procedure_params': {'key': 'sqlStoredProcedureParams', 'type': '[StoredProcedureParameter]'},
    }

    def __init__(self, *, sql_table_name: str=None, sql_query: str=None, sql_stored_procedure_name: str=None, sql_stored_procedure_params=None, **kwargs) -> None:
        super(DataPathSqlDataPath, self).__init__(sql_table_name=sql_table_name, sql_query=sql_query, sql_stored_procedure_name=sql_stored_procedure_name, sql_stored_procedure_params=sql_stored_procedure_params, **kwargs)
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .data_reference import DataReference


class DataLocationDataReference(DataReference):
    """DataLocationDataReference.

    :param type: Possible values include: 'None', 'AzureBlob',
     'AzureDataLake', 'AzureFiles', 'AzureSqlDatabase',
     'AzurePostgresDatabase', 'AzureDataLakeGen2', 'DBFS', 'AzureMySqlDatabase'
    :type type: str or ~designer.models.DataReferenceType
    :param azure_blob_reference:
    :type azure_blob_reference:
     ~designer.models.DataReferenceAzureBlobReference
    :param azure_data_lake_reference:
    :type azure_data_lake_reference:
     ~designer.models.DataReferenceAzureDataLakeReference
    :param azure_files_reference:
    :type azure_files_reference:
     ~designer.models.DataReferenceAzureFilesReference
    :param azure_sql_database_reference:
    :type azure_sql_database_reference:
     ~designer.models.DataReferenceAzureSqlDatabaseReference
    :param azure_postgres_database_reference:
    :type azure_postgres_database_reference:
     ~designer.models.DataReferenceAzurePostgresDatabaseReference
    :param azure_data_lake_gen2_reference:
    :type azure_data_lake_gen2_reference:
     ~designer.models.DataReferenceAzureDataLakeGen2Reference
    :param dbfs_reference:
    :type dbfs_reference: ~designer.models.DataReferenceDbfsReference
    :param azure_my_sql_database_reference:
    :type azure_my_sql_database_reference:
     ~designer.models.DataReferenceAzureMySqlDatabaseReference
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'azure_blob_reference': {'key': 'azureBlobReference', 'type': 'DataReferenceAzureBlobReference'},
        'azure_data_lake_reference': {'key': 'azureDataLakeReference', 'type': 'DataReferenceAzureDataLakeReference'},
        'azure_files_reference': {'key': 'azureFilesReference', 'type': 'DataReferenceAzureFilesReference'},
        'azure_sql_database_reference': {'key': 'azureSqlDatabaseReference', 'type': 'DataReferenceAzureSqlDatabaseReference'},
        'azure_postgres_database_reference': {'key': 'azurePostgresDatabaseReference', 'type': 'DataReferenceAzurePostgresDatabaseReference'},
        'azure_data_lake_gen2_reference': {'key': 'azureDataLakeGen2Reference', 'type': 'DataReferenceAzureDataLakeGen2Reference'},
        'dbfs_reference': {'key': 'dbfsReference', 'type': 'DataReferenceDbfsReference'},
        'azure_my_sql_database_reference': {'key': 'azureMySqlDatabaseReference', 'type': 'DataReferenceAzureMySqlDatabaseReference'},
    }

    def __init__(self, **kwargs):
        super(DataLocationDataReference, self).__init__(**kwargs)
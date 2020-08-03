# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .azure_files_reference_py3 import AzureFilesReference


class DataReferenceAzureFilesReference(AzureFilesReference):
    """DataReferenceAzureFilesReference.

    :param share:
    :type share: str
    :param uri:
    :type uri: str
    :param account:
    :type account: str
    :param relative_path:
    :type relative_path: str
    :param aml_data_store_name:
    :type aml_data_store_name: str
    """

    _attribute_map = {
        'share': {'key': 'share', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'},
        'account': {'key': 'account', 'type': 'str'},
        'relative_path': {'key': 'relativePath', 'type': 'str'},
        'aml_data_store_name': {'key': 'amlDataStoreName', 'type': 'str'},
    }

    def __init__(self, *, share: str=None, uri: str=None, account: str=None, relative_path: str=None, aml_data_store_name: str=None, **kwargs) -> None:
        super(DataReferenceAzureFilesReference, self).__init__(share=share, uri=uri, account=account, relative_path=relative_path, aml_data_store_name=aml_data_store_name, **kwargs)
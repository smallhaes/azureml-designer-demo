# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .datastore_setting import DatastoreSetting


class GraphDraftEntityDefaultDatastore(DatastoreSetting):
    """GraphDraftEntityDefaultDatastore.

    :param data_store_name:
    :type data_store_name: str
    """

    _attribute_map = {
        'data_store_name': {'key': 'dataStoreName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(GraphDraftEntityDefaultDatastore, self).__init__(**kwargs)
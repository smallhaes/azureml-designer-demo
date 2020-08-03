# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class GraphDatasetNode(Model):
    """GraphDatasetNode.

    :param id:
    :type id: str
    :param dataset_id:
    :type dataset_id: str
    :param data_path_parameter_name:
    :type data_path_parameter_name: str
    :param data_set_definition:
    :type data_set_definition:
     ~designer.models.GraphDatasetNodeDataSetDefinition
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'dataset_id': {'key': 'datasetId', 'type': 'str'},
        'data_path_parameter_name': {'key': 'dataPathParameterName', 'type': 'str'},
        'data_set_definition': {'key': 'dataSetDefinition', 'type': 'GraphDatasetNodeDataSetDefinition'},
    }

    def __init__(self, *, id: str=None, dataset_id: str=None, data_path_parameter_name: str=None, data_set_definition=None, **kwargs) -> None:
        super(GraphDatasetNode, self).__init__(**kwargs)
        self.id = id
        self.dataset_id = dataset_id
        self.data_path_parameter_name = data_path_parameter_name
        self.data_set_definition = data_set_definition
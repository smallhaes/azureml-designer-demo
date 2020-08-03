# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NodeOutputPort(Model):
    """NodeOutputPort.

    :param name:
    :type name: str
    :param documentation:
    :type documentation: str
    :param data_type_id:
    :type data_type_id: str
    :param pass_through_input_name:
    :type pass_through_input_name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'documentation': {'key': 'documentation', 'type': 'str'},
        'data_type_id': {'key': 'dataTypeId', 'type': 'str'},
        'pass_through_input_name': {'key': 'passThroughInputName', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, documentation: str=None, data_type_id: str=None, pass_through_input_name: str=None, **kwargs) -> None:
        super(NodeOutputPort, self).__init__(**kwargs)
        self.name = name
        self.documentation = documentation
        self.data_type_id = data_type_id
        self.pass_through_input_name = pass_through_input_name
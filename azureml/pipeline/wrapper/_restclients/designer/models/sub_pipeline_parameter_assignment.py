# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SubPipelineParameterAssignment(Model):
    """SubPipelineParameterAssignment.

    :param node_id:
    :type node_id: str
    :param parameter_name:
    :type parameter_name: str
    """

    _attribute_map = {
        'node_id': {'key': 'nodeId', 'type': 'str'},
        'parameter_name': {'key': 'parameterName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SubPipelineParameterAssignment, self).__init__(**kwargs)
        self.node_id = kwargs.get('node_id', None)
        self.parameter_name = kwargs.get('parameter_name', None)
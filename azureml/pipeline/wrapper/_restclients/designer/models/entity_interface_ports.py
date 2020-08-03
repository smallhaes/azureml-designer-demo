# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .node_port_interface import NodePortInterface


class EntityInterfacePorts(NodePortInterface):
    """EntityInterfacePorts.

    :param inputs:
    :type inputs: list[~designer.models.NodeInputPort]
    :param outputs:
    :type outputs: list[~designer.models.NodeOutputPort]
    """

    _attribute_map = {
        'inputs': {'key': 'inputs', 'type': '[NodeInputPort]'},
        'outputs': {'key': 'outputs', 'type': '[NodeOutputPort]'},
    }

    def __init__(self, **kwargs):
        super(EntityInterfacePorts, self).__init__(**kwargs)
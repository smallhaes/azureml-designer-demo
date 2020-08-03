# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NodeLayout(Model):
    """NodeLayout.

    :param x:
    :type x: float
    :param y:
    :type y: float
    :param width:
    :type width: float
    :param height:
    :type height: float
    """

    _attribute_map = {
        'x': {'key': 'x', 'type': 'float'},
        'y': {'key': 'y', 'type': 'float'},
        'width': {'key': 'width', 'type': 'float'},
        'height': {'key': 'height', 'type': 'float'},
    }

    def __init__(self, *, x: float=None, y: float=None, width: float=None, height: float=None, **kwargs) -> None:
        super(NodeLayout, self).__init__(**kwargs)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
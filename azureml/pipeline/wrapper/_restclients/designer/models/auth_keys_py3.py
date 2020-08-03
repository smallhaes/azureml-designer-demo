# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AuthKeys(Model):
    """AuthKeys.

    :param primary_key:
    :type primary_key: str
    :param secondary_key:
    :type secondary_key: str
    """

    _attribute_map = {
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
    }

    def __init__(self, *, primary_key: str=None, secondary_key: str=None, **kwargs) -> None:
        super(AuthKeys, self).__init__(**kwargs)
        self.primary_key = primary_key
        self.secondary_key = secondary_key
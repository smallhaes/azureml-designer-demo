# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AmlModuleNameMetaInfo(Model):
    """AmlModuleNameMetaInfo.

    :param module_namespace:
    :type module_namespace: str
    :param module_name:
    :type module_name: str
    :param module_version:
    :type module_version: str
    """

    _attribute_map = {
        'module_namespace': {'key': 'moduleNamespace', 'type': 'str'},
        'module_name': {'key': 'moduleName', 'type': 'str'},
        'module_version': {'key': 'moduleVersion', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AmlModuleNameMetaInfo, self).__init__(**kwargs)
        self.module_namespace = kwargs.get('module_namespace', None)
        self.module_name = kwargs.get('module_name', None)
        self.module_version = kwargs.get('module_version', None)
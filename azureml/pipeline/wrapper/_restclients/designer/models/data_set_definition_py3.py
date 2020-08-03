# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DataSetDefinition(Model):
    """DataSetDefinition.

    :param data_type_short_name:
    :type data_type_short_name: str
    :param parameter_name:
    :type parameter_name: str
    :param value:
    :type value: ~designer.models.DataSetDefinitionValueModel
    """

    _attribute_map = {
        'data_type_short_name': {'key': 'dataTypeShortName', 'type': 'str'},
        'parameter_name': {'key': 'parameterName', 'type': 'str'},
        'value': {'key': 'value', 'type': 'DataSetDefinitionValueModel'},
    }

    def __init__(self, *, data_type_short_name: str=None, parameter_name: str=None, value=None, **kwargs) -> None:
        super(DataSetDefinition, self).__init__(**kwargs)
        self.data_type_short_name = data_type_short_name
        self.parameter_name = parameter_name
        self.value = value
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .entity_interface_py3 import EntityInterface


class PipelineGraphEntityInterface(EntityInterface):
    """PipelineGraphEntityInterface.

    :param parameters:
    :type parameters: list[~designer.models.Parameter]
    :param ports:
    :type ports: ~designer.models.EntityInterfacePorts
    :param metadata_parameters:
    :type metadata_parameters: list[~designer.models.Parameter]
    :param data_path_parameters:
    :type data_path_parameters: list[~designer.models.DataPathParameter]
    :param data_path_parameter_list:
    :type data_path_parameter_list:
     list[~designer.models.DataSetPathParameter]
    """

    _attribute_map = {
        'parameters': {'key': 'parameters', 'type': '[Parameter]'},
        'ports': {'key': 'ports', 'type': 'EntityInterfacePorts'},
        'metadata_parameters': {'key': 'metadataParameters', 'type': '[Parameter]'},
        'data_path_parameters': {'key': 'dataPathParameters', 'type': '[DataPathParameter]'},
        'data_path_parameter_list': {'key': 'dataPathParameterList', 'type': '[DataSetPathParameter]'},
    }

    def __init__(self, *, parameters=None, ports=None, metadata_parameters=None, data_path_parameters=None, data_path_parameter_list=None, **kwargs) -> None:
        super(PipelineGraphEntityInterface, self).__init__(parameters=parameters, ports=ports, metadata_parameters=metadata_parameters, data_path_parameters=data_path_parameters, data_path_parameter_list=data_path_parameter_list, **kwargs)
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .model_management_error_response_py3 import ModelManagementErrorResponse


class RealTimeEndpointError(ModelManagementErrorResponse):
    """RealTimeEndpointError.

    :param code:
    :type code: str
    :param status_code:
    :type status_code: int
    :param message:
    :type message: str
    :param details:
    :type details: list[~designer.models.InnerErrorDetails]
    :param correlation:
    :type correlation: dict[str, str]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'status_code': {'key': 'statusCode', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[InnerErrorDetails]'},
        'correlation': {'key': 'correlation', 'type': '{str}'},
    }

    def __init__(self, *, code: str=None, status_code: int=None, message: str=None, details=None, correlation=None, **kwargs) -> None:
        super(RealTimeEndpointError, self).__init__(code=code, status_code=status_code, message=message, details=details, correlation=correlation, **kwargs)
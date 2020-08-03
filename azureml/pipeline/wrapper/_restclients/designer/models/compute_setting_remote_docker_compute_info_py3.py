# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .remote_docker_compute_info_py3 import RemoteDockerComputeInfo


class ComputeSettingRemoteDockerComputeInfo(RemoteDockerComputeInfo):
    """ComputeSettingRemoteDockerComputeInfo.

    :param address:
    :type address: str
    :param username:
    :type username: str
    :param password:
    :type password: str
    :param private_key:
    :type private_key: str
    """

    _attribute_map = {
        'address': {'key': 'address', 'type': 'str'},
        'username': {'key': 'username', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
        'private_key': {'key': 'privateKey', 'type': 'str'},
    }

    def __init__(self, *, address: str=None, username: str=None, password: str=None, private_key: str=None, **kwargs) -> None:
        super(ComputeSettingRemoteDockerComputeInfo, self).__init__(address=address, username=username, password=password, private_key=private_key, **kwargs)
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .person_py3 import Person


class CatalogExperimentAuthor(Person):
    """CatalogExperimentAuthor.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param avatar_url:
    :type avatar_url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'avatar_url': {'key': 'avatar_url', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, name: str=None, avatar_url: str=None, **kwargs) -> None:
        super(CatalogExperimentAuthor, self).__init__(id=id, name=name, avatar_url=avatar_url, **kwargs)
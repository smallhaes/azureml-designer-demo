# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PublishedPipeline(Model):
    """PublishedPipeline.

    :param total_run_steps:
    :type total_run_steps: int
    :param total_runs:
    :type total_runs: int
    :param parameters: This is a dictionary
    :type parameters: dict[str, str]
    :param rest_endpoint:
    :type rest_endpoint: str
    :param name:
    :type name: str
    :param description:
    :type description: str
    :param graph_id:
    :type graph_id: str
    :param published_date:
    :type published_date: datetime
    :param last_run_time:
    :type last_run_time: datetime
    :param last_run_status: Possible values include: 'NotStarted', 'Running',
     'Failed', 'Finished', 'Canceled'
    :type last_run_status: str or ~designer.models.PipelineRunStatusCode
    :param published_by:
    :type published_by: str
    :param tags: This is a dictionary
    :type tags: dict[str, str]
    :param version:
    :type version: str
    :param is_default:
    :type is_default: bool
    :param entity_status: Possible values include: 'Active', 'Deprecated',
     'Disabled'
    :type entity_status: str or ~designer.models.EntityStatus
    :param id:
    :type id: str
    :param etag:
    :type etag: str
    :param created_date:
    :type created_date: datetime
    :param last_modified_date:
    :type last_modified_date: datetime
    """

    _attribute_map = {
        'total_run_steps': {'key': 'totalRunSteps', 'type': 'int'},
        'total_runs': {'key': 'totalRuns', 'type': 'int'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'rest_endpoint': {'key': 'restEndpoint', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'graph_id': {'key': 'graphId', 'type': 'str'},
        'published_date': {'key': 'publishedDate', 'type': 'iso-8601'},
        'last_run_time': {'key': 'lastRunTime', 'type': 'iso-8601'},
        'last_run_status': {'key': 'lastRunStatus', 'type': 'str'},
        'published_by': {'key': 'publishedBy', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'version': {'key': 'version', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'entity_status': {'key': 'entityStatus', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'last_modified_date': {'key': 'lastModifiedDate', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(PublishedPipeline, self).__init__(**kwargs)
        self.total_run_steps = kwargs.get('total_run_steps', None)
        self.total_runs = kwargs.get('total_runs', None)
        self.parameters = kwargs.get('parameters', None)
        self.rest_endpoint = kwargs.get('rest_endpoint', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.graph_id = kwargs.get('graph_id', None)
        self.published_date = kwargs.get('published_date', None)
        self.last_run_time = kwargs.get('last_run_time', None)
        self.last_run_status = kwargs.get('last_run_status', None)
        self.published_by = kwargs.get('published_by', None)
        self.tags = kwargs.get('tags', None)
        self.version = kwargs.get('version', None)
        self.is_default = kwargs.get('is_default', None)
        self.entity_status = kwargs.get('entity_status', None)
        self.id = kwargs.get('id', None)
        self.etag = kwargs.get('etag', None)
        self.created_date = kwargs.get('created_date', None)
        self.last_modified_date = kwargs.get('last_modified_date', None)
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PipelineRunSummary(Model):
    """PipelineRunSummary.

    :param description:
    :type description: str
    :param run_number:
    :type run_number: int
    :param status_code: Possible values include: 'NotStarted', 'InDraft',
     'Preparing', 'Running', 'Failed', 'Finished', 'Canceled', 'Throttled',
     'Unknown'
    :type status_code: str or ~designer.models.PipelineStatusCode
    :param run_status: Possible values include: 'NotStarted', 'Starting',
     'Provisioning', 'Preparing', 'Queued', 'Running', 'Finalizing',
     'CancelRequested', 'Completed', 'Failed', 'Canceled', 'NotResponding'
    :type run_status: str or ~designer.models.RunStatus
    :param status_detail:
    :type status_detail: str
    :param start_time:
    :type start_time: datetime
    :param end_time:
    :type end_time: datetime
    :param graph_id:
    :type graph_id: str
    :param experiment_id:
    :type experiment_id: str
    :param experiment_name:
    :type experiment_name: str
    :param is_experiment_archived:
    :type is_experiment_archived: bool
    :param submitted_by:
    :type submitted_by: str
    :param tags: This is a dictionary
    :type tags: dict[str, str]
    :param properties: This is a dictionary
    :type properties: dict[str, str]
    :param aether_start_time:
    :type aether_start_time: datetime
    :param aether_end_time:
    :type aether_end_time: datetime
    :param run_history_start_time:
    :type run_history_start_time: datetime
    :param run_history_end_time:
    :type run_history_end_time: datetime
    :param unique_child_run_compute_targets:
    :type unique_child_run_compute_targets: list[str]
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

    _validation = {
        'unique_child_run_compute_targets': {'unique': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'run_number': {'key': 'runNumber', 'type': 'int'},
        'status_code': {'key': 'statusCode', 'type': 'str'},
        'run_status': {'key': 'runStatus', 'type': 'str'},
        'status_detail': {'key': 'statusDetail', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'graph_id': {'key': 'graphId', 'type': 'str'},
        'experiment_id': {'key': 'experimentId', 'type': 'str'},
        'experiment_name': {'key': 'experimentName', 'type': 'str'},
        'is_experiment_archived': {'key': 'isExperimentArchived', 'type': 'bool'},
        'submitted_by': {'key': 'submittedBy', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'aether_start_time': {'key': 'aetherStartTime', 'type': 'iso-8601'},
        'aether_end_time': {'key': 'aetherEndTime', 'type': 'iso-8601'},
        'run_history_start_time': {'key': 'runHistoryStartTime', 'type': 'iso-8601'},
        'run_history_end_time': {'key': 'runHistoryEndTime', 'type': 'iso-8601'},
        'unique_child_run_compute_targets': {'key': 'uniqueChildRunComputeTargets', 'type': '[str]'},
        'entity_status': {'key': 'entityStatus', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'last_modified_date': {'key': 'lastModifiedDate', 'type': 'iso-8601'},
    }

    def __init__(self, *, description: str=None, run_number: int=None, status_code=None, run_status=None, status_detail: str=None, start_time=None, end_time=None, graph_id: str=None, experiment_id: str=None, experiment_name: str=None, is_experiment_archived: bool=None, submitted_by: str=None, tags=None, properties=None, aether_start_time=None, aether_end_time=None, run_history_start_time=None, run_history_end_time=None, unique_child_run_compute_targets=None, entity_status=None, id: str=None, etag: str=None, created_date=None, last_modified_date=None, **kwargs) -> None:
        super(PipelineRunSummary, self).__init__(**kwargs)
        self.description = description
        self.run_number = run_number
        self.status_code = status_code
        self.run_status = run_status
        self.status_detail = status_detail
        self.start_time = start_time
        self.end_time = end_time
        self.graph_id = graph_id
        self.experiment_id = experiment_id
        self.experiment_name = experiment_name
        self.is_experiment_archived = is_experiment_archived
        self.submitted_by = submitted_by
        self.tags = tags
        self.properties = properties
        self.aether_start_time = aether_start_time
        self.aether_end_time = aether_end_time
        self.run_history_start_time = run_history_start_time
        self.run_history_end_time = run_history_end_time
        self.unique_child_run_compute_targets = unique_child_run_compute_targets
        self.entity_status = entity_status
        self.id = id
        self.etag = etag
        self.created_date = created_date
        self.last_modified_date = last_modified_date
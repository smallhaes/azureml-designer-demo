# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RunMetricDto(Model):
    """RunMetricDto.

    :param run_id:
    :type run_id: str
    :param metric_id:
    :type metric_id: str
    :param data_container_id:
    :type data_container_id: str
    :param metric_type:
    :type metric_type: str
    :param created_utc:
    :type created_utc: datetime
    :param name:
    :type name: str
    :param description:
    :type description: str
    :param label:
    :type label: str
    :param num_cells:
    :type num_cells: int
    :param data_location:
    :type data_location: str
    :param cells:
    :type cells: list[dict[str, object]]
    :param schema:
    :type schema: ~designer.models.RunMetricDtoSchema
    """

    _attribute_map = {
        'run_id': {'key': 'runId', 'type': 'str'},
        'metric_id': {'key': 'metricId', 'type': 'str'},
        'data_container_id': {'key': 'dataContainerId', 'type': 'str'},
        'metric_type': {'key': 'metricType', 'type': 'str'},
        'created_utc': {'key': 'createdUtc', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'num_cells': {'key': 'numCells', 'type': 'int'},
        'data_location': {'key': 'dataLocation', 'type': 'str'},
        'cells': {'key': 'cells', 'type': '[{object}]'},
        'schema': {'key': 'schema', 'type': 'RunMetricDtoSchema'},
    }

    def __init__(self, *, run_id: str=None, metric_id: str=None, data_container_id: str=None, metric_type: str=None, created_utc=None, name: str=None, description: str=None, label: str=None, num_cells: int=None, data_location: str=None, cells=None, schema=None, **kwargs) -> None:
        super(RunMetricDto, self).__init__(**kwargs)
        self.run_id = run_id
        self.metric_id = metric_id
        self.data_container_id = data_container_id
        self.metric_type = metric_type
        self.created_utc = created_utc
        self.name = name
        self.description = description
        self.label = label
        self.num_cells = num_cells
        self.data_location = data_location
        self.cells = cells
        self.schema = schema
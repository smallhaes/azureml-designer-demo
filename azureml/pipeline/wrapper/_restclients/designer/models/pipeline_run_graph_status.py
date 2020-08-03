# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class PipelineRunGraphStatus(Model):
    """PipelineRunGraphStatus.

    :param status:
    :type status: ~designer.models.PipelineRunGraphStatusStatus
    :param graph_nodes_status: This is a dictionary
    :type graph_nodes_status: dict[str, ~designer.models.GraphNodeStatusInfo]
    :param experiment_id:
    :type experiment_id: str
    :param is_experiment_archived:
    :type is_experiment_archived: bool
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'PipelineRunGraphStatusStatus'},
        'graph_nodes_status': {'key': 'graphNodesStatus', 'type': '{GraphNodeStatusInfo}'},
        'experiment_id': {'key': 'experimentId', 'type': 'str'},
        'is_experiment_archived': {'key': 'isExperimentArchived', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(PipelineRunGraphStatus, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.graph_nodes_status = kwargs.get('graph_nodes_status', None)
        self.experiment_id = kwargs.get('experiment_id', None)
        self.is_experiment_archived = kwargs.get('is_experiment_archived', None)
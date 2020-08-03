# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LinkedPipelineInfo(Model):
    """LinkedPipelineInfo.

    :param pipeline_type: Possible values include: 'TrainingPipeline',
     'RealTimeInferencePipeline', 'BatchInferencePipeline', 'Unknown'
    :type pipeline_type: str or ~designer.models.PipelineType
    :param module_node_id:
    :type module_node_id: str
    :param port_name:
    :type port_name: str
    :param linked_pipeline_draft_id:
    :type linked_pipeline_draft_id: str
    :param linked_pipeline_run_id:
    :type linked_pipeline_run_id: str
    :param is_direct_link:
    :type is_direct_link: bool
    """

    _attribute_map = {
        'pipeline_type': {'key': 'pipelineType', 'type': 'str'},
        'module_node_id': {'key': 'moduleNodeId', 'type': 'str'},
        'port_name': {'key': 'portName', 'type': 'str'},
        'linked_pipeline_draft_id': {'key': 'linkedPipelineDraftId', 'type': 'str'},
        'linked_pipeline_run_id': {'key': 'linkedPipelineRunId', 'type': 'str'},
        'is_direct_link': {'key': 'isDirectLink', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(LinkedPipelineInfo, self).__init__(**kwargs)
        self.pipeline_type = kwargs.get('pipeline_type', None)
        self.module_node_id = kwargs.get('module_node_id', None)
        self.port_name = kwargs.get('port_name', None)
        self.linked_pipeline_draft_id = kwargs.get('linked_pipeline_draft_id', None)
        self.linked_pipeline_run_id = kwargs.get('linked_pipeline_run_id', None)
        self.is_direct_link = kwargs.get('is_direct_link', None)
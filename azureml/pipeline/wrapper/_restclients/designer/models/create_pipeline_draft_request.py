# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CreatePipelineDraftRequest(Model):
    """CreatePipelineDraftRequest.

    :param name:
    :type name: str
    :param description:
    :type description: str
    :param pipeline_type: Possible values include: 'TrainingPipeline',
     'RealTimeInferencePipeline', 'BatchInferencePipeline', 'Unknown'
    :type pipeline_type: str or ~designer.models.PipelineType
    :param pipeline_draft_mode: Possible values include: 'None', 'Normal',
     'Custom'
    :type pipeline_draft_mode: str or ~designer.models.PipelineDraftMode
    :param graph:
    :type graph: ~designer.models.CreatePipelineDraftRequestGraph
    :param tags: This is a dictionary
    :type tags: dict[str, str]
    :param properties: This is a dictionary
    :type properties: dict[str, str]
    :param sub_pipelines_info:
    :type sub_pipelines_info:
     ~designer.models.CreatePipelineDraftRequestSubPipelinesInfo
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'pipeline_type': {'key': 'pipelineType', 'type': 'str'},
        'pipeline_draft_mode': {'key': 'pipelineDraftMode', 'type': 'str'},
        'graph': {'key': 'graph', 'type': 'CreatePipelineDraftRequestGraph'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'sub_pipelines_info': {'key': 'subPipelinesInfo', 'type': 'CreatePipelineDraftRequestSubPipelinesInfo'},
    }

    def __init__(self, **kwargs):
        super(CreatePipelineDraftRequest, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.pipeline_type = kwargs.get('pipeline_type', None)
        self.pipeline_draft_mode = kwargs.get('pipeline_draft_mode', None)
        self.graph = kwargs.get('graph', None)
        self.tags = kwargs.get('tags', None)
        self.properties = kwargs.get('properties', None)
        self.sub_pipelines_info = kwargs.get('sub_pipelines_info', None)
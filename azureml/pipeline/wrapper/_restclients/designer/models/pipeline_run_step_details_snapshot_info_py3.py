# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .snapshot_info_py3 import SnapshotInfo


class PipelineRunStepDetailsSnapshotInfo(SnapshotInfo):
    """PipelineRunStepDetailsSnapshotInfo.

    :param root_download_url:
    :type root_download_url: str
    :param snapshots: This is a dictionary
    :type snapshots: dict[str, ~designer.models.DownloadResourceInfo]
    """

    _attribute_map = {
        'root_download_url': {'key': 'rootDownloadUrl', 'type': 'str'},
        'snapshots': {'key': 'snapshots', 'type': '{DownloadResourceInfo}'},
    }

    def __init__(self, *, root_download_url: str=None, snapshots=None, **kwargs) -> None:
        super(PipelineRunStepDetailsSnapshotInfo, self).__init__(root_download_url=root_download_url, snapshots=snapshots, **kwargs)
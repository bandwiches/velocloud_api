from dataclasses import dataclass
from velocloud.models.image_update_scheduled_time import ImageUpdateScheduledTime


@dataclass
class ImageUpdateData:
    """Image Update Data"""
    buildNumber: str
    profileDeviceFamily: str
    profileVersion: str
    softwarePackageId: int
    softwarePackageName: str
    version: str
    windowDurationMins: int
    windowed: bool
    scheduledStartTime: ImageUpdateScheduledTime = None

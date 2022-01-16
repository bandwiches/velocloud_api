from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import unitName, unitType
from velocloud.models.device_settings_refs import DeviceSettingsRefs
from velocloud.models.segment_based_device_settings_data import SegmentBasedDeviceSettingsData


@dataclass
class SegmentBasedDeviceSettings:
    """Segment Based Device Settings"""
    name: unitName
    data: SegmentBasedDeviceSettingsData
    created: datetime = None  # datetime
    effective: datetime = None  # datetime
    modified: datetime = None  # datetime
    id: int = None
    type: unitType = None
    description: str = None
    configurationId: int = None
    schemaVersion: str = None
    version: str = None
    metadata: dict = None
    refs: DeviceSettingsRefs = None
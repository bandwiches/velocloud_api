from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import unitName, unitType
from velocloud.models.edge_device_settings_data import EdgeDeviceSettingsData
from velocloud.models.device_settings_refs import DeviceSettingsRefs


@dataclass
class EdgeDeviceSettings:
    """Edge Device Settings"""
    name: unitName
    data: EdgeDeviceSettingsData = None
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

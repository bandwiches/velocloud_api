from dataclasses import dataclass
from velocloud.models.enums import deviceSettingsRef


@dataclass
class DeviceSettingsAuthentication:
    """Device Settings - Authentication"""
    override: bool = None
    ref: deviceSettingsRef = None

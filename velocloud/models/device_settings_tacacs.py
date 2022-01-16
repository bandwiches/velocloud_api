from dataclasses import dataclass

from velocloud.models.enums import deviceSettingsRef


@dataclass
class DeviceSettingsTacacs:
    """Device Settings - TACACS"""
    ref: deviceSettingsRef = None
    sourceInterface: str = None

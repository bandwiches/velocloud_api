from dataclasses import dataclass


@dataclass
class DeviceSettingsSoftwareUpdateWindow:
    """Device Settings - Software Update Window"""
    day: int = None
    beginHour: int = None
    endHour: int = None

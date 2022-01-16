from dataclasses import dataclass

from velocloud.models.device_settings_software_update_window import DeviceSettingsSoftwareUpdateWindow


@dataclass
class DeviceSettingsSoftwareUpdate:
    """Device Settings - Software Update"""
    windowed: bool = None
    window: DeviceSettingsSoftwareUpdateWindow = None

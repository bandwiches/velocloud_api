from dataclasses import dataclass
from velocloud.models.device_settings_lan import DeviceSettingsLan
from velocloud.models.device_settings_routed_interface import DeviceSettingsRoutedInterface


@dataclass
class DeviceSettingsModel:
    """Device Settings Model"""
    lan: DeviceSettingsLan = None
    routedInterfaces: DeviceSettingsRoutedInterface = None

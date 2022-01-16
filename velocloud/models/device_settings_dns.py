from dataclasses import dataclass

from velocloud.models.enums import deviceSettingsRef


@dataclass
class Provider:
    """Provider
    This is a custom class.
    """
    ref: deviceSettingsRef = None


@dataclass
class DeviceSettingsDns:
    """Device Settings DNS"""
    override: bool = None
    primaryProvider: Provider = None
    backupProvider: Provider = None
    privateProviders: Provider = None

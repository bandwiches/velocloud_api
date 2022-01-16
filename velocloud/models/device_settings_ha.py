from dataclasses import dataclass


@dataclass
class DeviceSettingsHa:
    """Device Settings HA"""
    enabled: bool = None
    interface: str = None

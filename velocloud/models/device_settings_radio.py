from dataclasses import dataclass


@dataclass
class DeviceSettingsRadio:
    """Device Settings Radio"""
    band: str = None
    channel: str = None
    isEnabled: bool = None
    mode: str = None
    name: str = None
    radioId: int = None
    width: str = None

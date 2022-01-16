from dataclasses import dataclass
from velocloud.models.enums import deviceSettingsVpnType


@dataclass
class DeviceSettingsVpnHub:
    """Device Settings VPN Hub"""
    logicalId: str = None
    name: str = None
    type: deviceSettingsVpnType = None

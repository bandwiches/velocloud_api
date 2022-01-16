from dataclasses import dataclass

from velocloud.models.enums import deviceSettingsMulticastPimType


@dataclass
class DeviceSettingsMulticastPimOnWanOverlay:
    """Device Settings - Multicast - PIM on WAN Overlay"""
    enabled: bool = None
    type: deviceSettingsMulticastPimType = None
    sourceCidrIp: str = None
    sourceInterface: str = None

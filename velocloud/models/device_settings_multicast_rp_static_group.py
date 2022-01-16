from dataclasses import dataclass, field
from typing import List


@dataclass
class DeviceSettingsMulticastRpStaticGroup:
    """Device Settings - Multicast - RP Static Group"""
    multicastGroups: List(str) = field(default_factory=list)
    rpAddress: str = None

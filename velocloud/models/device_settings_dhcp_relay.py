from dataclasses import dataclass, field
from typing import List


@dataclass
class DeviceSettingsDhcpRelay:
    """Device Setting DHCP Relay"""
    enaled: bool = None
    servers: List(str) = field(default_factory=list)

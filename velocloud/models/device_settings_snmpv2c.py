from dataclasses import dataclass, field
from typing import List


@dataclass
class DeviceSettingsSnmpv2c:
    """Device Settings - SNMP v2c"""
    enabled: bool = None
    community: str = None
    allowedIp: List(str) = field(default_factory=list)  # IPv4Address?

from dataclasses import dataclass
from ipaddress import IPv4Address
from velocloud.models.enums import deviceSettingsNatRuleType


@dataclass
class DeviceSettingsNatRule:
    """Device Settings - NAT Rule"""
    type: deviceSettingsNatRuleType
    insideCidrIp: IPv4Address
    insideCidrPrefix: int
    insideNetmask: IPv4Address
    outsideCidrIp: IPv4Address
    outsideCidrPrefix: int
    outsideNetmask: IPv4Address
    outsidePort: int = None
    description: str = None
    insidePort: int = None

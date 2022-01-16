from dataclasses import dataclass
from ipaddress import IPv4Address
from velocloud.models.enums import routedInterfaceAddressingType


@dataclass
class DeviceSettingsRoutedInterfaceAddressing:
    """Device Settings Routed Interface Addressing"""
    type: routedInterfaceAddressingType = None
    cidrPrefix: int = None
    cidrIp: IPv4Address = None
    netmask: IPv4Address = None
    gateway: str = None
    username: str = None
    password: str = None

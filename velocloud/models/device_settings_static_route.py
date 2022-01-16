from dataclasses import dataclass
from ipaddress import IPv4Address


@dataclass
class DeviceSettingsStaticRoute:
    """Device Settings - Static Route"""
    destination: str = None
    netmask: IPv4Address = None
    sourceIp: IPv4Address = None
    gateway: IPv4Address = None
    cost: int = None
    preferred: bool = None
    description: str = None
    cidrPrefix: str = None
    wanInterface: str = None
    icmpProbeLogicalId: str = None
    vlanId: int = None
    advertise: bool = None
    subinterfaceId: int = None

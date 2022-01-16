from dataclasses import dataclass
from ipaddress import IPv4Address


@dataclass
class DeviceSettingsVrrpVirtualRouter:
    """Device Settings - VRRP Virtual Routers"""
    cidrIp: IPv4Address = None
    interface: str = None
    interval: int = None
    preempt: bool = None
    preemptDelay: int = None
    priority: int = None
    subinterfaceId: int = None
    vlanId: int = None
    vrid: int = None

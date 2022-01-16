from dataclasses import dataclass
from ipaddress import IPv4Address


@dataclass
class DeviceSettingsBgpNetwork:
    """Device Settings BGP Network"""
    cidrIp: IPv4Address = None
    cidrPrefix: int = None
    segmentId: str = None

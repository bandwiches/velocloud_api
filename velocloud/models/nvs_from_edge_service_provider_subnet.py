from dataclasses import dataclass
from ipaddress import IPv4Address


@dataclass
class NvsFromEdgeServiceProviderSubnet:
    """NVS From Edge Service Provider Subnet"""
    advertise: bool = None
    cidrIp: IPv4Address = None
    metric: int = None
    name: str = None
    cidrPrefix: str = None
    netMask: IPv4Address = None

from dataclasses import dataclass
from ipaddress import IPv4Address


@dataclass
class Destinations:
    """Destinations"""
    ip_addr: IPv4Address = None
    name: str = None

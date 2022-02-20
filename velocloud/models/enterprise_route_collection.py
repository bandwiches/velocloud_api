from dataclasses import dataclass, field
from ipaddress import IPv4Address
from typing import List
from velocloud.models.enterprise_route import EnterpriseRoute


@dataclass
class EnterpriseRouteCollection:
    """Enterprise Route Collection"""
    eligableExits: List(EnterpriseRoute) = field(default_factory=list)
    preferredExits: List(EnterpriseRoute) = field(default_factory=list)
    subnet: IPv4Address = None

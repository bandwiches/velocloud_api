from dataclasses import dataclass
from ipaddress import IPv4Address
from typing import List
from velocloud.models.enterprise_route import EnterpriseRoute


@dataclass
class EnterpriseUpdateEnterpriseRouteResult:
    """Enterprise Update Enterprise Route Result"""
    eligableExits: List(EnterpriseRoute)
    preferredExits: List(EnterpriseRoute)
    subnet: IPv4Address

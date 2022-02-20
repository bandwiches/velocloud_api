from dataclasses import dataclass
from datetime import datetime
from ipaddress import IPv4Address
from typing import List


@dataclass
class Edge:
    """Edge
    This is a custom class.
    """
    id: int
    name: str
    state: str


@dataclass
class EnterpriseGetEnterpriseMulticastRouteTableListResult:
    """Enterprise Get Enterprise Multicast Route Table List Result"""
    id: int
    enterpriseId: int
    cidrIp: IPv4Address
    cidrPrefix: int
    segmentId: int
    sourceAddress: IPv4Address
    created: datetime
    modified: datetime
    rpAddress: IPv4Address
    edgeCount: int
    edges: List(Edge)

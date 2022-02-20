from dataclasses import dataclass, field
from datetime import datetime
from ipaddress import IPv4Address
from typing import List
from velocloud.models.list_metadata import ListMetadata
from velocloud.models.count_result import CountResult


@dataclass
class Edge:
    """Edge
    This is a custom class.
    """
    id: int
    name: str
    state: str


@dataclass
class Data:
    """Data
    This is a custom class.
    """
    id: int = None
    enterpriseId: int = None
    cidrIp: IPv4Address = None
    cidrPrefix: int = None
    segmentId: int = None
    sourceAddress: IPv4Address = None
    created: datetime = None
    modified: datetime = None
    rpAddress: str = None
    edgeCount: int = None
    edges: List(Edge) = field(default_factory=list)
    edgeName: str = None
    segmentName: str = None


@dataclass
class EventGetProxyEventsListResult:
    """Event Get Proxy Events List Result"""
    data: List(Data) = field(default_factory=list)
    metaData: ListMetadata = None
    count: CountResult = None

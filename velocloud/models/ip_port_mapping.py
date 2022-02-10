from dataclasses import dataclass, field
from typing import List


@dataclass
class IpPortMapping:
    """IP Port Mapping"""
    subnets: List(str) = field(default_factory=list)
    tcpPorts: List(int) = field(default_factory=list)
    udpPorts: List(int) = field(default_factory=list)

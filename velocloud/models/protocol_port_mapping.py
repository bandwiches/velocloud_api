from dataclasses import dataclass, field
from typing import List


@dataclass
class ProtocolPortMapping:
    """Protocol Port Mapping"""
    tcpPorts: List(int) = field(default_factory=list)
    udpPorts: List(int) = field(default_factory=list)

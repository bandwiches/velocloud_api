from dataclasses import dataclass, field
from typing import List


@dataclass
class Dhcp:
    """DHCP
    This is a custom class.
    """
    enabled: bool = None
    leaseTimeSeconds: int = None


@dataclass
class Vlan:
    """VLAN
    This is a custom class.
    """
    name: str = None
    vlandId: int = None
    advertise: bool = None
    cost: int = None
    staticReserved: int = None
    dhcp: Dhcp = None


@dataclass
class Space:
    """Space
    This is a custom class.
    """
    cidrIp: str = None
    cidrPrefix: int = None
    maxVlans: int = None
    mode: str = None
    name: str = None
    branchCidrPrefix: int = None
    guest: bool = None
    vlans: List(Vlan) = field(default_factory=None)


@dataclass
class EnterpriseServiceNetworkData:
    """Enterprise Service Network Data"""
    zone: str = None
    spaces: List(Space) = field(default_factory=list)

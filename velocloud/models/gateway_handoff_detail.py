from dataclasses import dataclass, field
from typing import List
from velocloud.models.enums import gatewayHandoffType


@dataclass
class Subnet:
    """Subnet
    This is a custom class."""
    name: str = None
    routeCost: int = None  # 0 - 255
    cidrIp: str = None
    cidrPrefix: int = None
    encrypt: bool = None
    handOffType: gatewayHandoffType = None


@dataclass
class IcmpResponder:
    """ICMP Responder
    This is a custom class.
    """
    enabled: bool = None
    ipAddress: str = None
    mode: str = None


@dataclass
class IcmpProbe:
    """ICMP Probe
    This is a custom class.
    """
    enabled: bool = None
    probeType: str = None
    cTag: int = None
    sTag: int = None
    destinationIp: str = None
    frequencySeconds: int = None
    threshold: int = None


@dataclass
class GatewayHandoffDetail:
    """Gateway Handoff Detail"""
    type: str = None
    subnets: List(Subnet) = field(default_factory=list)
    icmpProbe: IcmpProbe = None
    icmpResponder: IcmpResponder = None

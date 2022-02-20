from dataclasses import dataclass


@dataclass
class Data:
    """Data
    This is a custom class.
    """
    type: str = None
    cTag: int = None
    sTag: int = None
    transportLanVLAN: str = None


@dataclass
class GatewayHandoffValueVlan:
    """Gateway Handoff Value VLAN"""
    wildcard: Data = None

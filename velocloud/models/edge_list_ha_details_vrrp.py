from dataclasses import dataclass


@dataclass
class EdgeListHaDetailsVrrp:
    """Edge List HA Details VRRP"""
    cidrIp: str = None
    interface: str = None
    interval: int = None
    preempt: bool = None
    preemptDelay: int = None
    priority: int = None
    subinterfaceId: int = None
    vlanId: int = None
    vrid: int = None

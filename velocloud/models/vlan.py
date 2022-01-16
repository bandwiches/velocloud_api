from dataclasses import dataclass


@dataclass
class Vlan:
    """Vlan"""
    name: str = None
    vlanId: int = None
    staticReserved: int = None

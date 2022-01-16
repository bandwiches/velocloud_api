from dataclasses import dataclass


@dataclass
class EnterpriseRoute:
    """Enterprise Route"""
    type: str = None
    exitType: str = None
    edgeId: int = None
    edgeName: str = None
    profileId: int = None
    cidrIp: str = None
    cost: int = None
    advertise: bool = None
    order: int = None

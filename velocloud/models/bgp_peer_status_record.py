from dataclasses import dataclass
from velocloud.models.enums import bgpPeerStatusState


@dataclass
class BgpPeerStatusRecord:
    """BGP Peer Status Record"""
    enterpriseLogicalId: str = None
    neighborAS: str = None
    neighborIp: str = None
    state: bgpPeerStatusState = None
    msgRcvd: int = None
    pfxRcvd: int = None
    msgSent: int = None
    upDownTime: int = None

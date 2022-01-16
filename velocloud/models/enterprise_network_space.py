from dataclasses import dataclass, field
from typing import List
from velocloud.models.enums import enterpriseNetworkSpaceMode
from velocloud.models.vlan import Vlan


@dataclass
class EnterpriseNetworkSpace:
    name: str = None
    mode: enterpriseNetworkSpaceMode = None
    cidrIp: str = None
    cidrPrefix: int = None
    maxVlans: int = None
    vlans: List(Vlan) = field(default_factory=list)

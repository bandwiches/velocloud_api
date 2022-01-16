from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import gatewayPoolHandoffType


@dataclass
class GatewayPool:
    """Gateway Pool"""
    id: int = None
    networkId: int = None
    enterpriseProxyId: int = None
    created: datetime = None  # datetime
    name: str = None
    description: str = None
    logicalId: str = None
    isDefault: bool = None
    handoffType: gatewayPoolHandoffType = None
    modified: datetime = None  # datetime

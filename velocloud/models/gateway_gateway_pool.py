from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import gatewayPoolHandoffType


@dataclass
class GatewayGatewayPool:
    """Gateway Gateway Pool"""
    id: int = None
    networkId: int = None
    enterpriseProxyId: int = None
    created: datetime = None
    name: str = None
    description: str = None
    logicalId: str = None
    isDefault: bool = None
    handOffType: gatewayPoolHandoffType = None
    modified: datetime = None
    gatewayPoolAssocId: int = None
    gatewayId: int = None

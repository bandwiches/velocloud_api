from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from velocloud.models.enums import gatewayPoolHandoffType
from velocloud.models.enterprise import Enterprise
from velocloud.models.gateway_pool_gateway import GatewayPoolGateway


@dataclass
class EnterpriseProxyGetEnterpriseProxyGatewayPoolsResultItem:
    """Enterprise Proxy Get Enterprise Proxy Gateway Pools Result Item"""
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
    enterprises: List(Enterprise) = field(default_factory=list)
    gateways: List(GatewayPoolGateway) = field(default_factory=list)

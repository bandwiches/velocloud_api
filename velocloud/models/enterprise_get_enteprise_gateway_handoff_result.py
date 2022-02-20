from dataclasses import dataclass
from datetime import datetime
from velocloud.models.gateway_handoff_value import GatewayHandoffValue


@dataclass
class EnterpriseGetEnterpriseGatewayHandoffResult:
    """Enterprise Get Enterprise Gateway Handoff Result"""
    enterpriseId: int
    value: GatewayHandoffValue
    id: int = None
    created: datetime = None
    name: str = None
    isPassword: bool = None
    dataType: str = None
    description: str = None
    modified: datetime = None

from dataclasses import dataclass
from velocloud.models.gateway_handoff_value import GatewayHandoffValue


@dataclass
class GatewayHandoff:
    """Gateway Handoff"""
    enterpriseId: int = None
    value: GatewayHandoffValue = None

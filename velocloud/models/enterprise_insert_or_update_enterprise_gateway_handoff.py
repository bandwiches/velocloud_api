from dataclasses import dataclass
from velocloud.models.gateway_handoff_value import GatewayHandoffValue


@dataclass
class EnterpriseInsertOrUpdateEnterpriseGatewayHandoff:
    """Enterprise Insert or Update Enterprise Gateway Handoff"""
    enterpriseId: int = None
    value: GatewayHandoffValue = None

from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import gatewayRole as gR


@dataclass
class GatewayRole:
    """Gateway Role"""
    created: datetime = None
    gatewayId: int = None
    gatewayRole: gR = None
    required: int = None

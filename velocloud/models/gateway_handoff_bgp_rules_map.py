from dataclasses import dataclass, field
from typing import List
from velocloud.models.gateway_handoff_bgp_rule import GatewayHandoffBgpRule


@dataclass
class GatewayHandoffBgpRulesMap:
    """Gateway Handoff BGP Rules Map"""
    rules: List(GatewayHandoffBgpRule) = field(default_factory=list)
    override: bool = None

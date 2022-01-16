from dataclasses import dataclass
from velocloud.models.firewall_rule_match import FirewallRuleMatch
from velocloud.models.enums import firewallRuleOutboundAction


@dataclass
class Action:
    """Firewall Action
    This is a custom class.
    """
    allow_or_deny: firewallRuleOutboundAction


@dataclass
class FirewallOutboundRule:
    """Firewall Outbound Rule"""
    match: FirewallRuleMatch
    action: Action
    name: str = None
    ruleLogicalId: str = None

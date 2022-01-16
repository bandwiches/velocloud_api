from dataclasses import dataclass
from velocloud.models.enums import firewallRuleActionType
from velocloud.models.firewall_rule_match import FirewallRuleMatch


@dataclass
class Nat:
    """Firewall NAT
    This is a custom class.
    """
    lan_ip: str
    lan_port: int = None
    outbound: bool = None


@dataclass
class Action:
    """Firewall Action
    This is a custom class.

    Args:
        interface (str): The name of the interface from which traffic should be forwarded
    """
    type: firewallRuleActionType
    nat: Nat
    interface: str
    subinterfaceId: int = None


@dataclass
class FirewallInboundRule:
    """Firewall Inbound Rule"""
    match: FirewallRuleMatch
    action: Action
    name: str = None
    ruleLogicalId: str = None

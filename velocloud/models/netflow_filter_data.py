from dataclasses import dataclass
from velocloud.models.enums import netflowFilterDataAction
from velocloud.models.netflow_filter_rule import NetflowFilterRule


@dataclass
class Action:
    """Netflow Filter Action
    This is a custom class.
    """
    allow_or_deny: netflowFilterDataAction


@dataclass
class NetflowFilterData:
    """Netflow Filter Data"""
    name: str
    match: NetflowFilterRule
    action: Action

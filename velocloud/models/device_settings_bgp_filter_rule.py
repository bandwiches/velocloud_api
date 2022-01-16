from dataclasses import dataclass, field
from typing import List
from velocloud.models.enums import bgpFilterRuleAction, bgpFilterRuleMatchType, bgpFilterRuleValueType


@dataclass
class Match:
    """Match
    This is a custom class.
    """
    exactMatch: bool = None
    type: bgpFilterRuleMatchType = None


@dataclass
class Value:
    """Value
    This is a custom class.
    """
    type: bgpFilterRuleValueType = None
    value: str = None


@dataclass
class Action:
    """Action
    This is a custom class.
    """
    type: bgpFilterRuleAction = None
    values: List(Value) = field(default_factory=list)


@dataclass
class DeviceSettingsBgpFilterRule:
    """Device Settings BGP Filter Rule"""
    action: Action = None
    match: Match = None

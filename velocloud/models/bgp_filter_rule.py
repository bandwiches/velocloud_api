from dataclasses import dataclass, field
from typing import List


@dataclass
class Match:
    """BGP Filter Rule Match
    This is a custom class.
    """
    exactMatch: bool = None
    type: str = None
    value: str = None


@dataclass
class ActionValue:
    """BGP Filter Rule Action Value
    This is a custom class.
    """
    type: str = None
    value: str = None


@dataclass
class Action:
    """BGP Filter Rule Action
    This is a custom class.
    """
    type: str = None
    values: List(ActionValue) = field(default_factory=list)


@dataclass
class BgpFilterRule:
    """BGP Filter Rule"""
    action: Action = None
    match: Match = None

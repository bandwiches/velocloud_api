from dataclasses import dataclass, field
from typing import List


@dataclass
class Value:
    """Value
    This is a custom class.
    """
    type: str = None
    value: str = None


@dataclass
class Match:
    """Match
    This is a custom class.
    """
    exactMatch: bool = None
    type: str = None
    value: str = None


@dataclass
class Action:
    """Action
    This is a custom class.
    """
    type: str = None
    values: List(Value) = field(default_factory=list)


@dataclass
class GatewayHandoffBgpRule:
    """Gateway Handoff BGP Rule"""
    action: Action = None
    match: Match = None

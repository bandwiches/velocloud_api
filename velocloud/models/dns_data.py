from dataclasses import dataclass, field
from typing import List


@dataclass
class Domain:
    """Domain
    This is a custom class.
    """
    rule: str = None
    description: str = None


@dataclass
class DnsData:
    """DNS Data"""
    primary: str = None
    secondary: str = None
    isPrivate: bool = None
    domains: List(Domain) = field(default_factory=list)

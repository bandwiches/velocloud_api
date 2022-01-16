from dataclasses import dataclass, field
from typing import List


@dataclass
class ConfigEdgeBgpFilterSet:
    """Config Edge BGP Filter Set"""
    ids: List(str) = field(default_factory=list)

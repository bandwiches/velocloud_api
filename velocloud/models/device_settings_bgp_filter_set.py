from dataclasses import dataclass, field
from typing import List


@dataclass
class DeviceSettingsBgpFilterSet:
    """Device Settings BGP Filter Set"""
    ids: List(str) = field(default_factory=list)

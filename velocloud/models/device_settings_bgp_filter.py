from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_bgp_filter_rule import DeviceSettingsBgpFilterRule


@dataclass
class DeviceSettingsBgpFilter:
    """Device Settings BGP Filter"""
    ids: List(str) = field(default_factory=list)
    name: str = None
    rules: List(DeviceSettingsBgpFilterRule) = field(default_factory=list)

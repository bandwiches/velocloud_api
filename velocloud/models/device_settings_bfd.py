from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_bfd_rule import DeviceSettingsBfdRule


@dataclass
class DeviceSettingsBfd:
    """Device Settings BFD"""
    enabled: bool = None
    override: bool = None
    rules: List(DeviceSettingsBfdRule) = field(default_factory=list)

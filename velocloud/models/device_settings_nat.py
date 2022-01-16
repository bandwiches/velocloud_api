from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_nat_dual_rule import DeviceSettingsNatDualRule
from velocloud.models.device_settings_nat_rule import DeviceSettingsNatRule


@dataclass
class DeviceSettingsNat:
    """Device Settings - NAT"""
    override: bool = None
    override: List(DeviceSettingsNatRule) = field(default_factory=list)
    dualRules: List(DeviceSettingsNatDualRule) = field(default_factory=list)

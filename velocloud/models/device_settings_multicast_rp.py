from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_multicast_rp_static_group import DeviceSettingsMulticastRpStaticGroup
from velocloud.models.enums import deviceSettingsMulticastRpType


@dataclass
class DeviceSettingsMulticastRp:
    """Device Settings - Multicast - RP"""
    type: deviceSettingsMulticastRpType = None
    staticGroups: List(DeviceSettingsMulticastRpStaticGroup) = field(default_factory=list)

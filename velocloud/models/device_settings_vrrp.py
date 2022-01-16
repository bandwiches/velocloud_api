from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_vrrp_virtual_router import DeviceSettingsVrrpVirtualRouter


@dataclass
class DeviceSettingsVrrp:
    """Device Settings - VRRP"""
    enabled: bool = None
    data: List(DeviceSettingsVrrpVirtualRouter) = field(default_factory=list)

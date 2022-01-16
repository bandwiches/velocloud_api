from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_dhcp_option import DeviceSettingsDhcpOption
from velocloud.models.device_settings_dhcp_relay import DeviceSettingsDhcpRelay


@dataclass
class DeviceSettingsDhcp:
    """Device Settings DHCP"""
    enabled: bool = None
    dhcpRelay: DeviceSettingsDhcpRelay = None
    leaseTimeSeconds: int = None
    baseDhcpAddr: int = None
    numDhcpAddr: int = None
    options: List(DeviceSettingsDhcpOption) = field(default_factory=list)
    override: bool = None

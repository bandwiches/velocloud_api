from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_lan_interface import DeviceSettingsLanInterface
from velocloud.models.device_settings_lan_network import DeviceSettingsLanNetwork
from velocloud.models.enums import lanVisibilityMode
from velocloud.models.subnet import Subnet


@dataclass
class Visibility:
    """Visibility
    This is a custom class.
    """
    override: bool = None
    mode: lanVisibilityMode = None


@dataclass
class DeviceSettingsLan:
    """Device Settings LAN"""
    interfaces: List(DeviceSettingsLanInterface) = field(default_factory=list)
    management: Subnet = None
    networks: List(DeviceSettingsLanNetwork) = field(default_factory=list)
    visibility: Visibility = None

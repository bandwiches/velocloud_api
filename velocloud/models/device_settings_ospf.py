from dataclasses import dataclass, field
from typing import List

from velocloud.models.device_settings_ospf_area import DeviceSettingsOspfArea
from velocloud.models.device_settings_ospf_bgp_redistribution import DeviceSettingsOspfBgpRedistribution
from velocloud.models.enums import deviceSettingsOspfDefaultRouteAdvertising, deviceSettingsOspfDefaultRouteType


@dataclass
class DeviceSettingsOspf:
    """Device Settings - OSPF"""
    enabled: bool = None
    areas: List(DeviceSettingsOspfArea) = field(default_factory=list)
    bgp: DeviceSettingsOspfBgpRedistribution = None
    defaultPrefixes: bool = None
    defaultRouteAdvertise: deviceSettingsOspfDefaultRouteAdvertising = None
    defaultRoutes: deviceSettingsOspfDefaultRouteType = None

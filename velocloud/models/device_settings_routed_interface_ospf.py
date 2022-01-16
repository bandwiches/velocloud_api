from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_routed_interface_ospf_filter import DeviceSettingsRoutedInterfaceOspfFilter


@dataclass
class DeviceSettingsRoutedInterfaceOspf:
    """Device Settings Routed Interface OSPF"""
    area: int = None
    authentication: bool = None
    authId: int = None
    authPassphrase: str = None
    cost: int = None
    deadTimer: int = None
    mode: str = None
    enabled: bool = None
    exclusionRoutes: List(dict) = field(default_factory=list)
    helloTimer: int = None
    inboundRouteLearning: DeviceSettingsRoutedInterfaceOspfFilter = None
    md5Authentication: bool = None
    MTU: int = None
    outboundRouteAdvertisement: DeviceSettingsRoutedInterfaceOspfFilter = None
    passive: bool = None
    vlanId: int = None

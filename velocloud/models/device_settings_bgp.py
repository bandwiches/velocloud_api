from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_bgp_filter import DeviceSettingsBgpFilter
from velocloud.models.device_settings_bgp_neighbor import DeviceSettingsBgpNeighbor
from velocloud.models.device_settings_bgp_network import DeviceSettingsBgpNetwork
from velocloud.models.device_settings_bgp_ospf_redistribution import DeviceSettingsBgpOspfRedistribution


@dataclass
class DefaultRoute:
    """Default Route
    This is a custom class.
    """
    enabled: bool = None
    advertise: str = None


@dataclass
class DeviceSettingsBgp:
    """Device Settings BGP"""
    enabled: bool = None
    override: bool = None
    ASN: str = None
    connectedRoutes: bool = None
    defaultRoute: DefaultRoute = None
    disableASPathCarryOver: bool = None
    filters: List(DeviceSettingsBgpFilter) = field(default_factory=list)
    holdtime: str = None
    isEdge: bool = None
    keepalive: str = None
    neighbors: List(DeviceSettingsBgpNeighbor) = field(default_factory=list)
    networks: List(DeviceSettingsBgpNetwork) = field(default_factory=list)
    ospf: DeviceSettingsBgpOspfRedistribution = None
    overlayPrefix: bool = None
    propagateUplink: bool = None
    routerId: str = None
    uplinkCommunity: str = None

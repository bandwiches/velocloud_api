from dataclasses import dataclass
from ipaddress import IPv4Address
from velocloud.models.device_settings_bgp_filter_set import DeviceSettingsBgpFilterSet
from velocloud.models.enums import BgpNeighborTag


@dataclass
class DeviceSettingsBgpNeighbor:
    """Device Settings BGP Neighbor"""
    neighborAS: str = None
    neighborIp: IPv4Address = None
    neighborTag: BgpNeighborTag = None
    inboundFilter: DeviceSettingsBgpFilterSet = None
    outboundFilter: DeviceSettingsBgpFilterSet = None
    localIp: IPv4Address = None
    maxHop: str = None
    allowAS: bool = None
    connect: str = None
    defaultRoute: bool = None
    holdtime: str = None
    keepalive: str = None
    enableMd5: bool = None
    md5Password: str = None

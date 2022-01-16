from dataclasses import dataclass
from velocloud.models.enums import BgpNeighborTag
from velocloud.models.config_edge_bgp_filter_set import ConfigEdgeBgpFilterSet


@dataclass
class ConfigEdgeBgpNeighbor:
    """Config Edge BGP Neighbor"""
    neighborAS: str = None
    neighborIp: str = None
    neighborTag: BgpNeighborTag = None
    inboundFilter: ConfigEdgeBgpFilterSet = None
    outboundFilter: ConfigEdgeBgpFilterSet = None
    allowAS: bool = None
    connect: str = None
    defaultRoute: bool = None
    holdtime: str = None
    keepalive: str = None
    enableMd5: bool = None
    md5Password: str = None

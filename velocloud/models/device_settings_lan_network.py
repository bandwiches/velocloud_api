from dataclasses import dataclass, field
from ipaddress import IPv4Address
from typing import List
from velocloud.models.device_settings_dhcp import DeviceSettingsDhcp
from velocloud.models.enums import igmpType, pimType


@dataclass
class Ospf:
    """OSPF
    This is a custom class.
    """
    enabled: bool = None
    override: bool = None
    area: int = None
    passiveInterface: bool = None


@dataclass
class Pim:
    """PIM
    This is a custom class."""
    enabled: bool = None
    type: pimType = None


@dataclass
class Igmp:
    """IGMP
    This is a custom class.
    """
    enabled: bool = None
    type: igmpType = None


@dataclass
class Multicast:
    """Multicast
    This is a custom class.
    """
    igmp: Igmp = None
    igmpHostQueryIntervalSeconds: int = None
    igmpMaxQueryResponse: int = None
    pim: Pim = None
    pimHelloTimerSeconds: int = None
    pimKeepAliveTimerSeconds: int = None
    pimPruneIntervalSeconds: int = None


@dataclass
class DeviceSettingsLanNetwork:
    """Device Settings LAN Network"""
    override: bool = None
    advertise: bool = None
    pingResponse: bool = True  # API has default value
    bindEdgeAddress: bool = None
    baseDhcpAddr: int = None
    cidrIp: IPv4Address = None
    cidrPrefix: int = None
    cost: int = None
    dhcp: DeviceSettingsDhcp = None
    disabled: bool = None
    interfaces: List(str) = field(default_factory=list)
    multicast: Multicast = None
    name: str = None
    netmask: str = None
    numDhcpAddr: int = None
    ospf: Ospf = None
    segmentId: int = None
    staticReserved: int = None
    vlanId: int = None
    vnfInsertion: bool = None

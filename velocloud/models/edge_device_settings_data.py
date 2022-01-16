from dataclasses import dataclass, field
from ipaddress import IPv4Address
from typing import List
from velocloud.models.bgp_filter_rule import BgpFilterRule
from velocloud.models.config_edge_bgp_neighbor import ConfigEdgeBgpNeighbor
from velocloud.models.enums import routedInterfaceAddressingType, rPF, edgeDeviceSettingsWanOverlay
from velocloud.models.edge_device_settings_data_dhcp_server import EdgeDeviceSettingsDataDhcpServer


# TACACS Section

@dataclass
class Tacacs:
    """TACACS
    This is a custom class.
    """
    ref: str = None
    sourceInterface: str = None


# Multi-Source QoS Section

@dataclass
class MultiSourceQos:
    """Multi-Source QoS
    This is a custom class.
    """
    enable: bool = None
    enabled: bool = None
    highRatio: int = None
    normalRatio: int = None
    lowRatio: int = None
    maxCapThreshold: int = None
    minCapThreshold: int = None


# SNMP Section

@dataclass
class SnmpV3User:
    """SNMP V3 User
    This is a custom class.
    """
    name: str = None
    passphrase: str = None
    authAlg: str = None
    privacy: bool = None
    encrAlg: str = None


@dataclass
class SnmpV3:
    """SNMP V3
    This is a custom class.
    """
    enabled: bool = None
    enable: bool = None
    users: List(SnmpV3User) = field(default_factory=list)


@dataclass
class SnmpV2c:
    """SNMP V2C
    This is a custom class.
    """
    enable: bool = None
    enabled: bool = None
    community: str = None
    allowedIp: List(str) = field(default_factory=list)


@dataclass
class Snmp:
    """SNMP
    This is a custom class.
    """
    port: int = None
    snmpv2c: SnmpV2c = None
    snmpv3: SnmpV3 = None


# VRRP Section

@dataclass
class VrrpData:
    """VRRP Data
    This is a custom class.
    """
    cidrIp: IPv4Address = None
    interface: str = None
    interval: int = None
    preempt: bool = None
    preemptDelay: int = None
    priority: int = None
    subinterfaceId: int = None
    vlanId: int = None
    vrid: int = None


@dataclass
class Vrrp:
    """VRRP
    This is a custom class.
    """
    enabled: bool = None
    data: List(VrrpData) = field(default_factory=list)


# Collector Section

@dataclass
class Collector:
    """Collector
    This is a custom class.
    """
    address: str = None  # IPv4Address?
    port: int = None


# VQM Section

@dataclass
class Vqm:
    """VQM
    This is a custom class.
    """
    enable: bool = None
    enabled: bool = None
    protocol: str = None
    collectors: List(Collector) = field(default_factory=list)


# Netflow Section

@dataclass
class Netflow:
    """Netflow
    This is a custom class.
    """
    enable: bool = None
    enabled: bool = None
    version: int = None
    collectors: List(Collector) = field(default_factory=list)


# DNS Section

@dataclass
class Provider:
    """Provider
    This is a custom class.
    """
    ref: str = None


@dataclass
class Dns:
    """DNS
    This is a custom class.
    """
    primaryProvider: Provider = None
    backupProvider: Provider = None
    privateProviders: Provider = None


# High Availability Section

@dataclass
class HighAvailabilityNode:
    """High Availability Node
    This is a custom class.
    """
    serialNumber: str = None
    instanceId: int = None


@dataclass
class HighAvailability:
    """High Availability
    This is a custom class.
    """
    enabled: bool = None
    interface: str = None
    nodes: List(HighAvailabilityNode) = field(default_factory=list)


# Routes Section

@dataclass
class RouteStatic:
    """Route Static
    This is a custom class.
    """
    destination: str = None
    netmask: IPv4Address = None
    sourceIp: IPv4Address = None
    gateway: str = None
    cost: int = None
    preferred: bool = None
    description: str = None
    cidrPrefix: str = None
    wanInterface: str = None
    icmpProbeLogicalId: str = None
    vlanId: int = None
    advertise: bool = None
    subinterfaceId: int = None


@dataclass
class Route:
    """Routes
    This is a custom class.
    """
    icmpProbes: List(dict) = field(default_factory=list)
    icmpResponders: List(dict) = field(default_factory=list)
    static: List(RouteStatic) = field(default_factory=list)


# OSPF Section

@dataclass
class OspfOutboundRouteAdvertisement:
    """OSPF Outbound Route Advertisement
    This is a custom class.
    """
    defaultAction: str = None
    filters: List(dict) = field(default_factory=list)


@dataclass
class OspfInboundRouteLearning:
    """OSPF Inbound Route Learning
    This is a custom class.
    """
    defaultAction: str = None
    filters: List(dict) = field(default_factory=list)


@dataclass
class Ospf:
    """OSPF
    This is a custom class.
    """
    area: int = None
    authentication: bool = None
    authId: int = None
    authPassphrase: str = None
    cost: int = None
    deadTimer: int = None
    mode: str = None
    enabled: bool = None
    helloTimer: int = None
    inboundRouteLearning: OspfInboundRouteLearning = None
    md5Authentication: bool = None
    MTU: int = None
    outboundRouteAdvertisement: OspfOutboundRouteAdvertisement = None
    passive: bool = None
    vlanId: int = None


# Routed Interfaces Section

@dataclass
class SubinterfaceAddressing:
    """Subinterface Addressing
    This is a custom class.
    """
    cidrIp: IPv4Address = None
    cidrPrefix: int = None
    gateway: str = None
    netmask: IPv4Address = None
    type: routedInterfaceAddressingType = None
    username: str = None
    password: str = None


@dataclass
class Subinterface:
    """Subinterface
    This is a custom class.
    """
    addressing: List(SubinterfaceAddressing) = field(default_factory=list)
    advertise: bool = None
    pingResponse: bool = True  # API has default value
    dhcpServer: EdgeDeviceSettingsDataDhcpServer = None
    disabled: bool = None
    natDirect: bool = None
    ospf: Ospf = None
    override: bool = None
    subinterfaceId: int = None
    subinterfaceType: str = None
    vlanId: int = None  # Static only
    trusted: bool = None
    rpf: rPF = None


@dataclass
class Layer2:
    """Layer 2
    This is a custom class.
    """
    autonegotiation: bool = None
    speed: str = None
    duplex: str = None
    MTU: int = None


@dataclass
class RoutedInterfaceAddressing:
    """Routed Interfaces Addressing
    This is a custom class.
    """
    type: routedInterfaceAddressingType = None
    cidrPrefix: int = None
    cidrIp: IPv4Address = None
    netmask: IPv4Address = None
    gateway: str = None
    username: str = None
    password: str = None


@dataclass
class RoutedInterface:
    """Routed Interfaces
    This is a custom class.
    """
    addressing: RoutedInterfaceAddressing = None
    advertising: bool = None
    pingResponse: bool = None
    disabled: bool = None
    dhcpServer: EdgeDeviceSettingsDataDhcpServer = None
    encryptOverlay: bool = None
    l2: Layer2 = None
    name: str = None
    natDirect: bool = None
    ospf: Ospf = None
    override: bool = None
    subinterfaces: List(Subinterface) = None
    vlanId: int = None  # Static only
    wanOverlay: edgeDeviceSettingsWanOverlay = None
    trusted: bool = None
    rpf: rPF = None
    underlayAccounting: bool = True  # API has default value


# LAN Section

@dataclass
class LanNetworkSecondaryIpAddressing:
    """LAN Network Sedcondary IP Addressing
    This is a custom class.
    """
    cidrIp: IPv4Address = None
    cidrPrefix: int = None
    netmask: IPv4Address = None


@dataclass
class LanNetworkSecondaryIp:
    """LAN Network Secondary IP
    This is a custom class.
    """
    advertise: bool = None
    override: bool = None
    pingResponse: bool = None
    addressing: LanNetworkSecondaryIpAddressing = None


@dataclass
class LanNetworkDhcpRelay:
    """LAN Network DHCP Relay
    This is a custom class.
    """
    servers: List(str) = field(default_factory=list)
    sourceFromSecondaryIp: bool = None


@dataclass
class LanNetworkDhcp:
    """LAN Network DHCP
    This is a custom class.
    """
    enabled: bool = None
    leaseTimeSeconds: int = None
    override: bool = None
    dhcpRelay: LanNetworkDhcpRelay = None


@dataclass
class LanNetwork:
    """LAN Network
    This is a custom class.

    Args:
        space (str):
        guest (bool):
        secure (bool):
        advertise (bool):
        pingResponse (bool):
        cost (int):
        dhcp (LanNetworkDhcp):
        staticReserved (int):
        netmask (IPv4Address):
        cidrPrefix (int):
        cidrIp (IPv4Address):
        baseDhcpAddr (int): An offset from the cidrIp including staticReserved (if any)
    """
    space: str = None
    guest: bool = None
    secure: bool = None
    advertise: bool = None
    pingResponse: bool = True  # API has default value
    cost: int = None
    dhcp: LanNetworkDhcp = None
    staticReserved: int = None
    netmask: IPv4Address = None
    cidrPrefix: int = None
    cidrIp: IPv4Address = None
    baseDhcpAddr: int = None
    numDhcpAddr: int = None
    name: str = None
    interfaces: List(str) = field(default_factory=list)
    vlanId: int = None
    managementIp: str = None
    disabled: bool = None
    secondaryIp: List(LanNetworkSecondaryIp) = field(default_factory=list)


@dataclass
class Lan:
    """LAN
    This is a custom class.
    """
    networks: List(LanNetwork) = field(default_factory=list)


# BGP Section

@dataclass
class Networks:
    """Networks
    This is a custom class.
    """
    cidrIp: str = None
    cidrPrefix: int = None


@dataclass
class BgpFilter:
    """BGP Filter
    This is a custom  class.
    """
    id: str = None
    name: str = None
    rules: List(BgpFilterRule) = field(default_factory=list)


@dataclass
class Bgp:
    """BGP
    This is a custom class.
    """
    ASN: str = None
    connectedRoutes: bool = None
    disableASPathCarryOver: bool = None
    enabled: bool = None
    filters: List(BgpFilter) = field(default_factory=list)
    holdtime: str = None
    keepalive: str = None
    neighbors: List(ConfigEdgeBgpNeighbor) = field(default_factory=list)
    networks: List(Networks) = field(default_factory=list)
    overlayPrefix: bool = None
    propagateUplink: bool = None
    routerId: str = None
    uplinkCommunity: int = None


# Main Class Section

@dataclass
class EdgeDeviceSettingsData:
    """Edge Device Settings Data"""
    bgp: Bgp = None
    lan: Lan = None
    routedInterfaces: List(RoutedInterface) = field(default_factory=list)
    routes: Route = None
    ha: HighAvailability = None
    dns: Dns = None
    netflow: Netflow = None
    vqm: Vqm = None
    vrrp: Vrrp = None
    snmp: Snmp = None
    multiSourceQos: MultiSourceQos = None
    tacacs: Tacacs = None

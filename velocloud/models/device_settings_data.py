from dataclasses import dataclass, field
from typing import List
from ipaddress import IPv4Address
from velocloud.models.enums import rPF
from velocloud.models.device_settings_vpn_hub import DeviceSettingsVpnHub


# VPN Section

@dataclass
class VpnEdgeToEdgeDetailDynamic:
    """VPN - Edge to Edge Detail - Dynamic
    This is a custom class.
    """
    enabled: bool = None
    type: str = None
    timeout: int = None


@dataclass
class VpnEdgeToEdgeDetail:
    """VPN - Edge to Edge Detail
    This is a custom class.
    """
    useCloudGateway: bool = None
    encryptionProtocol: str = None
    dynamic: VpnEdgeToEdgeDetailDynamic = None
    vpnHubs: List(DeviceSettingsVpnHub) = field(default_factory=list)
    autoSelectVpnHubs: bool = None


@dataclass
class VpnEdgeToEdgeHub:
    """VPN - Edge to Edge Hub
    This is a custom class.
    """
    enabled: bool = None
    ref: str = None
    vpnHubs: List(DeviceSettingsVpnHub) = field(default_factory=list)


@dataclass
class Vpn:
    """VPN
    This is a custom class.
    """
    enabled: bool = None
    edgeToDataCenter: bool = None
    ref: str = None
    edgeToEdgeHub: VpnEdgeToEdgeHub = None
    edgeToEdge: bool = None
    edgeToEdgeDetail: VpnEdgeToEdgeDetail = None
    conditionalBackhaul: bool = None
    backHaulEdges: List(DeviceSettingsVpnHub) = field(default_factory=list)


# Models Section

@dataclass
class MV_LanInterfaceLayer2:
    """Models Virtual  - LAN - Interface - Layer 2"""
    autonegotiation: bool = None
    speed: str = None
    duplex: str = None
    MTU: int = None


@dataclass
class MV_LanInterface:
    """Models Virtual - LAN - Interface
    This is a custom class.
    """
    space: str = None
    name: str = None
    type: str = None
    cwp: bool = None
    portMode: str = None
    untaggedVlan: str = None
    disabled: bool = None
    l2: MV_LanInterfaceLayer2 = None
    vlanIds: List(int) = field(default_factory=list)


@dataclass
class MV_Lan:
    """Models Virtual - LAN
    This is a custom class.
    """
    interfaces: List()


@dataclass
class MV_RoutedInterfaceL2:
    """Models Virtual - Routed Interface - Layer 2
    This is a custom class.
    """
    autonegotiation: bool = None
    speed: str = None
    duplex: str = None
    MTU: int = None


@dataclass
class MV_RoutedInterfaceOspfoutboundRouteAdvertisement:
    """Models Virtual - Routed Interface - OSPF Outbound Route Advertisement
    This is a custom class.
    """
    defaultAction: str = None
    filters: List(dict) = field(default_factory=list)


@dataclass
class MV_RoutedInterfaceOspfInboundRouteLearning:
    """Models Virtual - Routed Interface - OSPF Inbound Route Learning
    This is a custom class.
    """
    defaultAction: str = None
    filters: List(dict) = field(default_factory=list)


@dataclass
class MV_RoutedInterfaceOspf:
    """Models Virtual - Routed Interface - OSPF
    This is a custom class.
    """
    enabled: bool = None
    area: int = None
    authentication: bool = None
    authId: int = None
    authPassphrase: str = None
    helloTimer: int = None
    deadTimer: int = None
    mode: str = None
    md5Authentication: bool = None
    cost: int = None
    MTU: int = None
    passive: bool = None
    inboundRouteLearning: MV_RoutedInterfaceOspfInboundRouteLearning = None
    outboundRouteAdvertisement: MV_RoutedInterfaceOspfoutboundRouteAdvertisement = None


@dataclass
class MV_RoutedInterfaceAddressing:
    """Models Virtual - Routed Interface - Addressing
    This is a custom class.
    """
    type: str = None
    cidrPrefix: int = None
    cidrIp: IPv4Address = None
    netmask: IPv4Address = None
    gateway: str = None


@dataclass
class MV_RoutedInterface:
    """Models Virtual - Routed Interface
    This is a custom class.
    """
    name: str = None
    disabled: bool = None
    addressing: MV_RoutedInterfaceAddressing = None
    wanOverlay: str = None
    natDirect: bool = None
    ospf: MV_RoutedInterfaceOspf = None
    vlanId: int = None
    l2: MV_RoutedInterfaceL2 = None
    underlayAccounting: bool = True  # API has default value
    trusted: bool = None
    rpf: rPF = None


@dataclass
class ModelsVirtual:
    """Models Virtual
    This is a custom class.
    """
    routedInterfaces: List(MV_RoutedInterface) = field(default_factory=list)
    lan: MV_Lan = None


@dataclass
class Models:
    """Models
    This is a custom class.
    """
    virtual: ModelsVirtual = None


# Multi-Source QoS Section

@dataclass
class MultiSourceQos:
    """Multi-Source QoS
    This is a custom class.
    """
    enabled: bool = None
    highRatio: int = None
    normalRatio: int = None
    lowRatio: int = None
    maxCapThreshold: int = None
    minCapThreshold: int = None


# SNMP Section

@dataclass
class Snmpv3User:
    """SNMPv3 User
    This is a custom class.
    """
    name: str = None
    passphrase: str = None
    authAlg: str = None
    privacy: bool = None
    encrAlg: str = None


@dataclass
class Snmpv3:
    """SNMPv3
    This is a custom class.
    """
    enabled: bool = None
    users: List(Snmpv3User) = field(default_factory=list)


@dataclass
class Snmpv2c:
    """SNMPv2c
    This is a custom class.
    """
    enabled: bool = None
    community: str = None
    allowedIp: List(str) = field(default_factory=list)


@dataclass
class Snmp:
    """SNMP
    This is a custom class.
    """
    port: int = None
    snmpv2c: Snmpv2c = None
    snmpv3: Snmpv3 = None


# Collector Section

@dataclass
class Collector:
    """Collector
    This is a custom class.
    """
    address: str = None
    port: int = None


# VQM Section

@dataclass
class Vqm:
    """VQM
    This is a custom class.
    """
    enabled: bool = None
    protocol: str = None
    collectors: List(Collector) = field(default_factory=list)


# Netflow Section

@dataclass
class Netflow:
    """Netflow
    This is a custom class.
    """
    enabled: bool = None
    version: int = None
    collectors: List(Collector) = field(default_factory=list)


# Layer 2 Settings Section

@dataclass
class L2Settings:
    """Layer 2
    This is a custom class.
    """
    overrideARPTimeout: bool = None
    arpStaleTimeoutMinutes: int = None
    arpDeadTimeoutMinutes: int = None
    arpCleanupTimeoutMinutes: int = None


# Radio Settings Section

@dataclass
class Radio:
    """Radio
    This is a custom class.
    """
    radioId: int = None
    isEnabled: bool = None
    name: str = None
    band: str = None
    channel: str = None
    width: str = None
    mode: str = None


@dataclass
class RadioSettings:
    """Radio Settings
    This is a custom class.
    """
    country: str = None
    radios: List(Radio) = field(default_factory=list)


# Software Update Section

@dataclass
class SoftwareUpdateWindow:
    """Software Update Window
    This is a custom class.
    """
    day: int = None
    beginHour: int = None
    endHour: int = None


@dataclass
class SoftwareUpdate:
    """Software Update
    This is a custom class.
    """
    windowed: bool = None
    window: SoftwareUpdateWindow = None


# Authentication Section

@dataclass
class Authentication:
    """Authentication
    This is a custom class.
    """
    ref: str = None


# DNS Section

@dataclass
class DnsProvider:
    """DNS Provider
    This is a custom class.
    """
    ref: str = None


@dataclass
class Dns:
    """DNS
    This is a custom class.
    """
    primaryProvider: DnsProvider = None
    backupProvider: DnsProvider = None
    privateProviders: DnsProvider = None


# BGP Section

@dataclass
class Bgp:
    """BGP
    This is a custom section.
    """
    enabled: bool = None
    asn: str = None
    neighbors: List(dict) = field(default_factory=list)


# OSPF Section

@dataclass
class OspfArea:
    """OSPF Area
    This is a custom class.
    """
    id: int = None
    name: str = None
    type: str = None


@dataclass
class Ospf:
    """OSPF
    This is a custom class.
    """
    enabled: bool = None
    areas: List(OspfArea) = field(default_factory=list)


# LAN Section

@dataclass
class LanAllocation:
    """LAN Allocation
    This is a custom class.
    """
    ref: str = None
    assignableVlans: List(int) = field(default_factory=list)
    managementVlans: List(int) = field(default_factory=list)


@dataclass
class Lan:
    """LAN
    This is a custom class.
    """
    allocation: LanAllocation = None


# Main Class

@dataclass
class DeviceSettingsData:
    """Device Settings Data"""
    lan: Lan = None
    ospf: Ospf = None
    bgp: Bgp = None
    dns: Dns = None
    authentication: Authentication = None
    softwareUpdate: SoftwareUpdate = None
    radioSettings: RadioSettings = None
    l2Settings: L2Settings = None
    netflow: Netflow = None
    vqm: Vqm = None
    snmp: Snmp = None
    multiSourceQos: MultiSourceQos = None
    models: Models = None
    vpn: Vpn = None

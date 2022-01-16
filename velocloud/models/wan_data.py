from dataclasses import dataclass, field
from ipaddress import IPv4Address
from typing import List
from velocloud.models.enums import wanDataLinkDiscovery, wanDataLinkMode, wanDataLinkType


@dataclass
class Network:
    """Network
    This is a custom class.
    """
    mode: str = None
    type: str = None
    name: str = None
    logicalId: str = None
    interface: str = None
    internalId: str = None
    ipAddress: IPv4Address = None
    isp: str = None
    lastActive: int = None


@dataclass
class StaticSla:
    """Static SLA
    This is a custom class.
    """
    latencyMs: int = None
    jitterMs: int = None
    lossPct: int = None


@dataclass
class CoS:
    """CoS (Class of Service)
    This is a custom class.
    """
    id: str = None
    name: str = None
    dscpTags: List(str) = field(default_factory=list)
    staticSLA: StaticSla = None
    bandwidthPct: int = None
    bandwidthGuaranteed: bool = None
    defaultClassOfService: bool = None


@dataclass
class ClassesOfService:
    """Classes of Service
    This is a custom class.
    """
    classId: int = None
    classesOfService: List(CoS) = field(default_factory=list)


@dataclass
class Link:
    """Link
    This is a custom class.
    """
    logicalId: str = None
    internalId: str = None
    discovery: wanDataLinkDiscovery = None
    mode: wanDataLinkMode = None
    type: wanDataLinkType = None
    name: str = None
    isp: str = None
    publicIpAddress: IPv4Address = None
    sourceIpAddress: IPv4Address = None
    nextHopIpAddress: IPv4Address = None
    customVlanId: bool = None
    vlanId: int = None
    enable8021P: bool = None
    priority8021P: int = None
    virtualIpAddress: str = None
    dynamicBwAdjustmentEnabled: bool = None
    bwMeasurement: str = None
    upstreamMbps: str = None
    downstreamMbps: str = None
    backupOnly: bool = None
    hotStandby: bool = None
    minActiveLinks: int = None
    overheadBytes: int = None
    udpHolePunching: bool = None
    MTU: int = None
    pmtudDisabled: bool = None
    mplsNetwork: str = None
    dscpTag: str = None
    staticSlaEnabled: bool = None
    classesofServiceEnabled: bool = None
    strictIpPrecedence: bool = None
    encryptOverlay: bool = None
    staticSLA: StaticSla = None
    classesOfService: ClassesOfService = None
    interfaces: List(str) = field(default_factory=list)
    lastActive: str = None


@dataclass
class WanData:
    """WAN Data"""
    links: List() = field(default_factory=list)
    networks: List(Network) = field(default_factory=list)

from dataclasses import dataclass, field
from ipaddress import IPv4Address
from typing import List
from velocloud.models.enums import bgpCommunityMappingPriorityMode, gatewayHandoffType, gatewayHandoffValueType
from velocloud.models.gateway_handoff_segment_metadata import GatewayHandoffSegmentMetadata
from velocloud.models.gateway_handoff_value_bgp_priority_setup_auto_as import GatewayHandoffValueBgpPrioritySetupAutoAs
from velocloud.models.gateway_handoff_value_bgp_priority_setup_auto_med import GatewayHandoffValueBgpPrioritySetupAutoMed
from velocloud.models.gateway_handoff_bgp_rules_map import GatewayHandoffBgpRulesMap
from velocloud.models.gateway_handoff_value_vlan import GatewayHandoffValueVlan


@dataclass
class OverrideSubnets:
    """Override Subnets
    This is a custom class.
    """
    wildcard: List(dict) = field(default_factory=list)


@dataclass
class OverrideLocalAddressData:
    """Override Local Address Data
    This is a custom class.
    """
    cidrIp: str = None
    cidrPrefix: int = None
    useForPrivate: bool = None
    advertiseViaBgp: bool = None


@dataclass
class OverrideLocalAddress:
    """Override Local Address
    This is a custom class.
    """
    wildcard: OverrideLocalAddressData = None


@dataclass
class OverrideBgpMap:
    """Override BGP Map
    This is a custom class.
    """
    wildcard: GatewayHandoffBgpRulesMap = None


@dataclass
class OverrideBgpData:
    """Override BGP Data
    This is a custom class.
    """
    enabled: bool = None
    ASN: str = None
    neighborIp: str = None
    neighborASN: str = None
    encryption: bool = None


@dataclass
class OverrideBgp:
    """OVerride BGP
    This is a custom class.
    """
    wildcard: OverrideBgpData = None


@dataclass
class OverrideVlanData:
    """Override VLAN Data
    This is a custom class.
    """
    type: str = None
    cTag: int = None
    sTag: int = None
    transportLanVLAN: str = None


@dataclass
class OverrideVlan:
    """Override VLAN
    This is a custom class.
    """
    wildcard: OverrideVlanData = None


@dataclass
class Overrides:
    """Overrides
    This is a custom class.
    """
    VLAN: OverrideVlan = None
    bgp: OverrideBgp = None
    bgpInboundMap: OverrideBgpMap = None
    bgpOutboundMap: OverrideBgpMap = None
    localAddress: OverrideLocalAddress = None
    subnets: OverrideSubnets = None


@dataclass
class Bgp:
    """BGP
    This is a custom class.
    """
    enabled: bool = None
    ASN: str = None
    neighborIp: IPv4Address = None
    neighborASN: str = None
    encryption: bool = None


@dataclass
class Subnet:
    """Subnet
    This is a custom class.
    """
    name: str = None
    cidrIp: IPv4Address = None
    cidrPrefix: IPv4Address = None
    encrypt: bool = None
    handOffType: gatewayHandoffType = None
    routeCost: int = None  # 0 - 255


@dataclass
class StaticRoutes:
    """Static Routes
    This is a custom class.
    """
    override: bool = None
    subnets: List(Subnet) = field(default_factory=list)


@dataclass
class LocalAddress:
    """Local Address
    This is a custom class.
    """
    cidrIp: str = None
    cidrPrefix: int = None
    useForPrivate: bool = None
    advertiseViaBgp: bool = None
    override: bool = None


@dataclass
class CommunityMappingPriority:
    """Community Mapping Priority
    This is a custom class.
    """
    community: str = None
    community2: str = None
    priority: int = None


@dataclass
class CommunityMapping:
    """Community Mapping
    This is a custom class.
    """
    enabled: bool = False  # API has default value
    priorityMode: bgpCommunityMappingPriorityMode = None
    priorities: List(CommunityMappingPriority) = field(default_factory=list)
    communityAdditive: bool = None


@dataclass
class BgpPrioritySetup:
    """BGP Priority Setup
    This is a custom class.
    """
    autoAs: GatewayHandoffValueBgpPrioritySetupAutoAs = None
    autoMed: GatewayHandoffValueBgpPrioritySetupAutoMed = None
    communityMapping: CommunityMapping = None


@dataclass
class GatewayHandoffValueSegments:
    """Gateway Handoff Value Segments"""
    segments: dict = None
    segment: GatewayHandoffSegmentMetadata = None
    bgpPrioritySetup: BgpPrioritySetup = None
    type: gatewayHandoffValueType = None
    override: bool = None
    cTag: int = None
    sTag: int = None
    localAddress: LocalAddress = None
    staticRoutes: StaticRoutes = None
    bgp: Bgp = None
    bgpInboundMap: GatewayHandoffBgpRulesMap = None
    bgpOutboundMap: GatewayHandoffBgpRulesMap = None
    VLAN: GatewayHandoffValueVlan = None
    overrides: Overrides = None

from dataclasses import dataclass, field
from ipaddress import IPv4Address
from typing import List
from velocloud.models.control_plane_data_nvs_from_edge_provider import ControlPlaneDataNvsFromEdgeProvider


# IPSec Gateway Detail Section

@dataclass
class IpsecGatewayDetailItem:
    """IPSec Gateway Detail Item
    This is a custom class.
    """
    enabled: bool = None
    strictHostCheck: bool = None
    strictHostCheckDN: str = None


@dataclass
class IpsecGatewayDetail:
    """IPSec Gateway Detail
    This is a custom class.
    """
    data: IpsecGatewayDetailItem = None


# NVS From Edge Section

@dataclass
class NVSFromEdge:
    """NVS From  Edge
    This is a custom class.
    """
    enabled: bool = None
    providers: List(ControlPlaneDataNvsFromEdgeProvider) = field(default_factory=list)


# VPN Section

@dataclass
class MiniEdgeDetailProfileIsolation:
    """Mini(mal) Edge Detail Profile Isolation
    This is a custom class.
    """
    enabled: bool = None
    isolateDynamic: bool = None


@dataclass
class MiniEdgeDetailDynamic:
    """Mini(mal) Edge Detail Dyanmic
    This is a custom class.
    """
    enabled: bool = None
    timeout: int = None
    type: str = None


@dataclass
class MiniEdgeDetail:
    """Mini(mal) Edge Detail
    This is a custom class.
    """
    dynamic: MiniEdgeDetailDynamic = None
    encryptionProtocol: str = None
    profileIsolation: MiniEdgeDetailProfileIsolation = None
    useCloudGateway: bool = None
    vpnHubs: List(dict) = field(default_factory=list)
    autoSelectVpnHubs: bool = None


@dataclass
class MiniEdge:
    """Mini(mal) Edge
    This is a custom class.
    """
    logicalId: str = None
    name: str = None


@dataclass
class MiniEdgeListItem(MiniEdge):
    """Mini(mal) Edge List Item
    This is a custom class.
    """
    isolateDynamic: int = None
    profileLogicalId: str = None


@dataclass
class VPN:
    """VPN
    This is a custom class.
    """
    conditionalBackhaul: bool = None
    backHaulEdges: List(MiniEdge) = field(default_factory=list)
    dataCenterEdges: List(MiniEdge) = field(default_factory=list)
    edgeToDataCenter: bool = None
    edgeToEdge: bool = None
    edgeToEdgeDetail: MiniEdgeDetail = None
    edgeToEdgeList: List(MiniEdgeListItem) = field(default_factory=list)


# Gateway Selection Section

@dataclass
class GatewaySelectionDetail:
    """Detail
    This is a custom class.
    """
    ipAddress: IPv4Address
    logicalId: str
    name: str


@dataclass
class GatewaySelection:
    """Gateway Selection
    This is a custom class.
    """
    mode: str = None
    primary: str = None
    primaryDetail: GatewaySelectionDetail = None
    secondary: str = None
    secondaryDetail: GatewaySelectionDetail = None
    super: str = None
    superDetail: GatewaySelectionDetail = None


# Main Class

@dataclass
class ControlPlaneData:
    """Control Plane Data"""
    gatewaySelection: GatewaySelection
    vpn: VPN = None
    nvsFromEdge: NVSFromEdge = None
    ipsecGatewayDetail: IpsecGatewayDetail = None

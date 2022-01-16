from dataclasses import dataclass, field
from typing import List
from velocloud.models.enums import nvsProvider, nvsType, nvsProviderCategory, nvsTunnelingProtocol
from velocloud.models.nvs_from_edge_service_provider_subnet import NvsFromEdgeServiceProviderSubnet
from velocloud.models.nvs_from_edge_service_provider_server_config import NvsFromEdgeServiceProviderServerConfig
from velocloud.models.nvs_from_edge_site_data import NvsFromEdgeSiteData


@dataclass
class VpnCredentialsWithlinks:
    """VPN Credentials with Links
    This is a custom class.
    """
    useAllPublicWanLinks: bool = None
    links: List(NvsFromEdgeSiteData) = field(default_factory=list)


@dataclass
class Bgp:
    """BGP
    This is a custom class.
    """
    enabled: bool = None


@dataclass
class PeerSubnet:
    """Peer Subnet
    This is a custom class.
    """
    alwaysReachable: bool = None
    subnets: List(NvsFromEdgeServiceProviderSubnet) = field(default_factory=list)
    version: str = None


@dataclass
class Subnets:
    """Subnets
    This is a custom class.
    """
    subnets: List(NvsFromEdgeServiceProviderSubnet) = field(default_factory=list)


@dataclass
class ControlPlaneDataNvsFromEdgeProvider:
    """Control Plane Data NVS From Edge Provider"""
    enabled: bool = None
    provider: nvsProvider = None
    type: nvsType = None
    automateDeployment: bool = None
    providerCategory: nvsProviderCategory = None
    routingPolicy: str = None
    tunnelingProtocol: nvsTunnelingProtocol = None
    sharedIkeAuth: bool = None
    sourceSubnets: Subnets = None
    peerSubnets: PeerSubnet = None
    bgp: Bgp = None
    primaryServer: NvsFromEdgeServiceProviderServerConfig = None
    backupServer: NvsFromEdgeServiceProviderServerConfig = None
    keepBackupServerConnected: bool = None
    version: str = None
    vpnCredentialsWithlinks: VpnCredentialsWithlinks = None

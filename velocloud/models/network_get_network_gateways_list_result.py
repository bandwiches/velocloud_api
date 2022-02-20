from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from velocloud.models.enums import edgeActivationState, endpointPkiMode as ePM, enterpriseGatewayState, gatewayServiceState
from velocloud.models.list_metadata import ListMetadata
from velocloud.models.count_result import CountResult
from velocloud.models.gateway_certificate import GatewayCertificate
from velocloud.models.gateway_enterprise_assoc import GatewayEnterpriseAssoc
from velocloud.models.enterprise import Enterprise
from velocloud.models.gateway_handoff_detail import GatewayHandoffDetail
from velocloud.models.gateway_handoff_edge import GatewayHandoffEdge
from velocloud.models.gateway_gateway_pool import GatewayGatewayPool
from velocloud.models.gateway_role import GatewayRole
from velocloud.models.site import Site


@dataclass
class UtilizationDetail:
    """Utilization Detail
    This is a custom class.
    """
    load: int = None
    overall: int = None
    cpu: int = None
    memory: int = None


@dataclass
class IpsecGatewayDetail:
    """IPSec Gateway Detail
    This is a custom class.
    """
    enabled: bool = None
    strictHostCheck: bool = None
    strictHostCheckDN: str = None


@dataclass
class EnterpriseAssociationCount:
    """Enterprise Association Count
    This is a custom class.
    """
    wildcard: int = None


@dataclass
class ConnectedEdge:
    """Connected Edge
    This is a custom class.
    """
    vceid: str = None


@dataclass
class Data:
    """Data
    This is a custom class.
    """
    activationKey: str = None
    activationState: edgeActivationState = None
    activationTime: datetime = None
    buildNumber: str = None
    certificates: List(GatewayCertificate) = None
    connectedEdges: int = None
    connectedEdgeList: List(ConnectedEdge) = None
    created: datetime = None
    dataCenters: List(dict) = None
    description: str = None
    deviceId: str = None
    dnsName: str = None
    endpointPkiMode: ePM = None
    enterpriseAssociations: List(GatewayEnterpriseAssoc) = field(default_factory=list)
    enterpriseAssociationCount: EnterpriseAssociationCount = None
    enterprises: List(Enterprise) = field(default_factory=list)
    enterpriseProxyId: int = None
    gatewayState: enterpriseGatewayState = None
    handOffDetail: GatewayHandoffDetail = None
    handOffEdges: List(GatewayHandoffEdge) = field(default_factory=list)
    id: int = None
    ipAddress: str = None
    ipsecGatewayDetail: IpsecGatewayDetail = None
    isLoadBalanced: bool = None
    lastContact: str = None
    logicalId: str = None
    modified: datetime = None
    name: str = None
    networkId: int = None
    pools: List(GatewayGatewayPool) = field(default_factory=list)
    privateIpAddress: str = None
    roles: List(GatewayRole) = field(default_factory=list)
    serviceState: gatewayServiceState = None
    serviceUpSince: str = None
    site: Site = None
    siteId: int = None
    softwareVersion: str = None
    systemUpSince: str = None
    utilization: int = None
    utilizationDetail: UtilizationDetail = None
    poolsCount: int = None
    certificatesCount: int = None


@dataclass
class NetworkGetNetworkGatewaysListResult:
    """Network Get Network Gateways List Result"""
    data: List(Data) = field(default_factory=list)
    metaData: ListMetadata = None
    count: CountResult = None

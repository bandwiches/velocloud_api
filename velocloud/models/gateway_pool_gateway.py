from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from velocloud.models.gateway_handoff_detail import GatewayHandoffDetail


@dataclass
class IpsecGatewayDetail:
    """IPSec Gateway Detail
    This is a custom class.
    """
    enabled: bool = None
    strictHostCheck: bool = None
    strictHostCheckDN: str = None


@dataclass
class ConnectedEdgeListItem:
    """Connected Edge List Item
    This is a custom class.
    """
    vceid: str = None


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
class GatewayPoolGateway:
    """Gateway Pool Gateway"""
    gatewayPoolAssocId: int = None
    poolName: str = None
    id: int = None
    created: datetime = None  # datetime
    networkId: int = None
    enterpriseProxyId: int = None
    siteId: int = None
    activationKey: str = None
    activationState: str = None
    activationTime: datetime = None  # datetime
    softwareVersion: str = None
    buildNumber: str = None
    utilization: int = None
    utilizationDetail: UtilizationDetail = None
    connectedEdges: int = None
    connectedEdgeList: List(ConnectedEdgeListItem) = field(default_factory=list)
    deviceId: str = None
    logicalId: str = None
    name: str = None
    gatewayState: str = None
    description: str = None
    dnsName: str = None
    isLoadBalanced: int = None
    privateIpAddress: str = None
    ipAddress: str = None
    lastContact: datetime = None  # datetime
    systemUpSince: datetime = None  # datetime
    serviceUpSince: datetime = None  # datetime
    serviceState: str = None
    endpointPkiMode: str = None
    handOffDetail: GatewayHandoffDetail = None
    ipsecGatewayDetail: IpsecGatewayDetail = None
    modified: datetime = None  # datetime

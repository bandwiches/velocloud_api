from dataclasses import dataclass, field
from typing import List
from velocloud.models.enums import edgeActivationState, edgeHaState, edgeServiceState, edgeState, endpointPkiMode as EPM, haType, tinyint
from velocloud.models.edge_certificate import EdgeCertificate
from velocloud.models.edge_license import EdgeLicense
from velocloud.models.link import Link
from velocloud.models.site import Site
from velocloud.models.get_enterprise_edge_cloud_services_result import GetEnterpriseEdgeCloudServicesResult
from velocloud.models.get_enterprise_edge_vnfs_result import GetEnterpriseEdgeVnfsResult


@dataclass
class HighAvailability:
    """High Availability
    This is a custom class.
    """
    type: haType = None
    data: dict = None


@dataclass
class EdgeOverride:
    """Edge Override
    This is a custom class.
    """
    deviceSettings: bool = None
    firewall: bool = None
    firewallDisabled: bool = None
    qos: bool = None


@dataclass
class Enterprise:
    """Enterprise
    This is a custom class.
    """
    id: int = None
    name: str = None


@dataclass
class ImageUpdate:
    """Image Update
    This is a custom class.
    """
    version: str = None
    buildNumber: str = None


@dataclass
class Operator:
    """Operator
    This is a custom class.
    """
    id: int = None
    name: str = None
    isEdgeSpecific: bool = None
    imageUpdate: ImageUpdate = None


@dataclass
class Configuration:
    """Configuration
    This is a custom class.
    """
    operator: Operator = None
    enterprise: Enterprise = None
    edgeOverrides: EdgeOverride = None


@dataclass
class EnterpriseGetEnterpriseEdgeListResultItem:
    """Enterprise Get Enterprise Edge LIst REsult Item"""
    activationKey: str
    activationKeyExpires: str
    activationState: edgeActivationState
    activationTime: str
    alertsEnabled: tinyint
    buildNumber: str
    created: str  # datetime?
    customInfo: str
    description: str
    deviceFamily: str
    deviceId: str
    dnsName: str
    edgeState: edgeState
    edgeStateTime: str
    endpointPkiMode: EPM
    enterpriseId: int
    haLastContact: str
    haPreviousState: edgeHaState
    haSerialNumber: str
    haState: edgeHaState
    id: int
    isLive: int
    lastContact: str
    logicalId: str
    modelNumber: str
    modified: str
    name: str
    operatorAlertsEnabled: tinyint
    selfMacAddress: str
    serialNumber: str
    serviceState: edgeServiceState
    serviceUpSince: str
    siteId: int
    softwareUpdated: str
    softwareVersion: str
    systemUpSince: str
    factorySoftwareVersion: str = None
    factoryBuildNumber: str = None
    certificates: List(EdgeCertificate) = field(default_factory=list)
    configuration: Configuration = None
    ha: HighAvailability = None
    licenses: List(EdgeLicense) = field(default_factory=list)
    links: List(Link) = field(default_factory=list)
    recentLinks: List(Link) = field(default_factory=list)
    site: Site = None
    isHub: bool = None
    cloudServices: List(GetEnterpriseEdgeCloudServicesResult) = field(default_factory=list)
    nvsFromEdge: List(GetEnterpriseEdgeCloudServicesResult) = field(default_factory=list)
    vnfs: GetEnterpriseEdgeVnfsResult = None

from dataclasses import dataclass, field
from typing import List
from velocloud.models.edge_certificate import EdgeCertificate
from velocloud.models.edge_license import EdgeLicense
from velocloud.models.link import Link
from velocloud.models.site import Site
from velocloud.models.enums import edgeActivationState, edgeHaState, edgeServiceState, edgeState, endpointPkiMode as EPM, unitType, tinyint


@dataclass
class HighAvailability:
    """High Availability
    This is a custom class.
    """
    type: unitType = None
    date: dict = None


@dataclass
class EnterpriseModule:
    """Enterprise Module
    This is a custom class.
    """
    edgeSpecificData: dict = None
    isEdgeSpecific: tinyint = None
    name: str = None
    type: unitType = None
    version: str = None


@dataclass
class Enterprise:
    """Enterprise
    This is a custom class.
    """
    id: int = None
    modules: List(EnterpriseModule) = None
    name: str = None


@dataclass
class OperatorModule:
    """Operator Module
    This is a custom class.
    """
    isEdgeSpecific: tinyint = None
    name: str = None
    type: unitType = None


@dataclass
class Operator:
    """Operator
    This is a custom class.
    """
    id: int = None
    modules: List(OperatorModule) = field(default_factory=list)
    name: str = None


@dataclass
class Configuration:
    """Configuration
    This is a custom class.
    """
    operator: Operator = None
    enterprise: Enterprise = None


@dataclass
class EnterpriseGetEnterpriseEdgesResultItem:
    """Enterprise Get Enterprise Edges Result Item"""
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
    lastContact: str  # datetime?
    logicalId: str
    modelNumber: str
    modified: str  # datetime?
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
    isSoftwareVersionSupportedByVco: bool = None

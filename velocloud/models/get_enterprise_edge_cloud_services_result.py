from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProviderData:
    """Provider Data
    This is a custom class.
    """
    primaryServer: str = None
    secondaryServer: str = None
    automateDeployment: bool = None
    enableTunnels: bool = None
    sharedIkeAuth: bool = None
    maxTunnelsPerIkeIdentity: int = None
    provider: str = None


@dataclass
class Provider:
    """Provider
    This is a custom class.
    """
    name: str = None
    id: int = None
    logicalId: str = None
    data: ProviderData = None


@dataclass
class SiteData:
    """Data
    This is a custom class.
    """
    ikeIdType: str = None
    pskType: str = None
    ikeId: str = None


@dataclass
class Site:
    """Site
    This is a custom class.
    """
    id: int = None
    logicalId: str = None
    data: SiteData = None


@dataclass
class GetEnterpriseEdgeCloudServicesResult:
    """Get Enterprise Edge Cloud Services Result"""
    state: str = None
    timestamp: datetime = None  # datetime
    link: str = None
    local_interface_ip: str = None
    local_public_ip: str = None
    nvs_ip: str = None
    pathId: str = None
    segmentId: int = None
    segmentLogicalId: str = None
    site: Site = None
    provider: Provider = None

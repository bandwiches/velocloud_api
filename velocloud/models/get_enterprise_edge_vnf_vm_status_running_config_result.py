from dataclasses import dataclass
from datetime import datetime


@dataclass
class LicenseServer:
    """License Server
    This is a custom class.
    """
    url: str = None
    apiKey: str = None


@dataclass
class ManagementServer:
    """Management Server
    This is a custom class.
    """
    authKey: str = None
    primary: str = None
    secondary: str = None


@dataclass
class VendorSpecificData:
    """Vendor Specific Data"""
    configTemplateName: str = None
    authCodeValidationTimeStamp: str = None
    managementServer: ManagementServer = None
    authCode: str = None
    authCodeValidated: bool = None
    deviceGroupName: str = None
    licenseServer: LicenseServer = None
    deviceTemplateName: str = None


@dataclass
class Edge:
    """Edge
    This is a custom class.
    """
    logicalId: str = None
    ref: str = None


@dataclass
class Status:
    """Status
    This is a custom class.
    """
    logicalId: str = None
    ref: str = None


@dataclass
class License:
    """License
    This is a custom class.
    """
    logicalId: str = None
    ref: str = None


@dataclass
class GetEnterpriseEdgeVnfVmStatusRunningConfigResult:
    """GetEnterpriseEdgeVnfVmStatusRunningConfigResult"""
    cidrPrefix: int = None
    insertionEnabled: bool = None
    vmPowerOff: bool = None
    vendor: str = None
    uuid: str = None
    uuidTimestamp: datetime = None  # datetime
    license: License = None
    service: Status = None
    hostname: str = None
    enabled: bool = None
    vlanId: int = None
    cidrIp: str = None
    netmask: str = None
    edge: Edge = None
    modifiedTimestamp: int = None
    dns: str = None
    vendorSpecificData: VendorSpecificData = None
    vmDeploy: bool = None
    type: str = None
    gateway: str = None
    dnsSecondary: str = None

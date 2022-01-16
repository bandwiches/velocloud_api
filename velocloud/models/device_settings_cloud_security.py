from dataclasses import dataclass, field
from typing import List
from velocloud.models.css_zscaler_sublocations import CssZscalerSubLocations
from velocloud.models.device_settings_cloud_security_site import DeviceSettingsCloudSecuritySite
from velocloud.models.enums import cloudSecurityTunnelingProtocol, deviceSettingsRef


@dataclass
class SubLocations:
    """Sub Locations
    This is a custom class.
    """
    subLocationList: List(CssZscalerSubLocations) = field(default_factory=list)


@dataclass
class Provider:
    """Provider
    This is a custom class.
    """
    ref: deviceSettingsRef = None


@dataclass
class GreProp:
    """GRE Proposal
    This is a custom class.
    """
    keepaliveIntervalSecs: int = None  # 0 - 30
    keepaliveRetries: int = None  # 0 - 10


@dataclass
class IkeProp:
    """IKE Proposal
    This is a custom class.
    """
    protocolVersion: int = None


@dataclass
class Config:
    """Config
    This is a custom class.
    """
    tunnelingProtocol: cloudSecurityTunnelingProtocol = None
    authenticationAlgorithm: str = None
    encryptionAlgorithm: str = None
    redirect: str = None
    IKEPROP: IkeProp = None
    GREPROP: GreProp = None


@dataclass
class DeviceSettingsCloudSecurity:
    """Device Settings Cloud Security"""
    enabled: bool = None
    override: bool = None
    config: Config = None
    provider: Provider = None
    sites: List(DeviceSettingsCloudSecuritySite) = field(default_factory=list)
    subLocations: SubLocations = None

from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import deviceSettingsSecurityVnfVmVendor


@dataclass
class Service:
    """Service
    This is a custom class.
    """
    logicalId: str = None
    ref: str = None  # pattern: deviceSettings:securityVnf:service


@dataclass
class License:
    """License
    This is a custom class.
    """
    logicalId: str = None
    ref: str = None  # pattern: deviceSettings:securityVnf:license


@dataclass
class Edge:
    """Edge
    This is a custom class.
    """
    logicalId: str = None
    ref: str = None  # pattern: deviceSettings:vnfs:edge


@dataclass
class DeviceSettingsSecurityVnfVm:
    """Device Settings - Security VNF VM"""
    type: str = None  # pattern: securityVnf
    vendor: deviceSettingsSecurityVnfVmVendor = None
    edge: Edge = None
    license: License = None
    service: Service = None
    uuid: str = None
    uuidTimestamp: datetime = None  # datetime

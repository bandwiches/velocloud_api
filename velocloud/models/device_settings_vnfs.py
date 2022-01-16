from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_security_vnf_vm import DeviceSettingsSecurityVnfVm


@dataclass
class SecurityVnf:
    """Security VNF
    This is a custom class.
    """
    vms: List(DeviceSettingsSecurityVnfVm) = field(default_factory=list)


@dataclass
class Edge:
    """Edge
    This is a custom class.
    """
    logicalId: str = None
    ref: str = None  # pattern: deviceSettings:vnfs:edge


@dataclass
class DeviceSettingsVnfs:
    """Device Settings - VNFS"""
    edge: Edge = None
    hasVnfs: bool = None
    securityVnf: SecurityVnf = None

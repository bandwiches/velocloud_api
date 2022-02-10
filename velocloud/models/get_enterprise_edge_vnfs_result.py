from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from velocloud.models.get_enterprise_edge_vnf_vm_status_running_config_result import GetEnterpriseEdgeVnfVmStatusRunningConfigResult


@dataclass
class HealthStats:
    """Health Stats
    This is a custom class.
    """
    cpuPercent: int = None
    memoryInMB: int = None
    storageInGB: int = None
    state: str = None
    runningConfig: GetEnterpriseEdgeVnfVmStatusRunningConfigResult = None


@dataclass
class Status:
    """Status
    This is a custom class.
    """
    vmStatus: str = None
    status: str = None
    description: str = None
    serialNumber: str = None
    isEdgeActive: bool = None
    vnfInsertionEnabled: bool = None
    runningConfig: GetEnterpriseEdgeVnfVmStatusRunningConfigResult = None
    healthStatsTimestamp: datetime = None   # datetime
    healthStats: HealthStats = None


@dataclass
class VendorSpecificData:
    """Vendor Specific Data
    This is a custom class.
    """
    deviceGroupName: str = None
    deviceTemplateName: str = None


@dataclass
class Data:
    """Data
    This is a custom class.
    """
    type: str = None
    vendor: str = None
    ref: str = None
    vendorSpecificData: VendorSpecificData = None
    vmDeploy: bool = None
    vmPowerOff: bool = None
    vlanId: int = None
    cidrIp: str = None
    hostname: str = None
    insertionEnabled: bool = None
    instanceId: int = None


@dataclass
class Vm:
    """VM
    This is a custom class.
    """
    id: int = None
    logicalId: str = None
    data: Data = None
    status: Status = None


@dataclass
class SecurityVnf:
    """Security VNF
    This is a custom class.
    """
    vms: List(Vm) = field(default_factory=list)


@dataclass
class GetEnterpriseEdgeVnfsResult:
    """Get Enterprise Edge VNFS Result"""
    securityVnf: SecurityVnf = None

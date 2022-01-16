from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_vpn_profile_isolation import DeviceSettingsVpnProfileIsolation
from velocloud.models.device_settings_vpn_profile_isolation_deprecated import DeviceSettingsVpnProfileIsolationDeprecated
from velocloud.models.enums import deviceSettingsRef
from velocloud.models.device_settings_vpn_hub import DeviceSettingsVpnHub


@dataclass
class EdgeToEdgeDetailIsolationGroup:
    """Edge to Edge Detail - Isolation Group
    This is a custom class.
    """
    logicalId: str = None


@dataclass
class EdgeToEdgeDetailDynamic:
    """Edge to Edge Detail - Dynamic
    This is a custom class.
    """
    enabled: bool = None
    isolation: DeviceSettingsVpnProfileIsolation = None
    type: str = None
    timeout: int = None


@dataclass
class EdgeToEdgeDetail:
    """Edge to Edge Detail
    This is a custom class.
    """
    autoSelectVpnHubs: bool = None
    dynamic: EdgeToEdgeDetailDynamic = None
    encryptionProtocol: str = None
    profileIsolation: DeviceSettingsVpnProfileIsolationDeprecated = None
    isolation: DeviceSettingsVpnProfileIsolation = None
    isolationGroupId: str = None
    isolationGroups: List(EdgeToEdgeDetailIsolationGroup) = field(default_factory=list)
    useCloudGateway: bool = None
    vpnHubs: List(DeviceSettingsVpnHub) = field(default_factory=list)


@dataclass
class EdgeToEdgeHub:
    """Edge to Edge Hub
    This is a custom class.
    """
    enaled: bool = None
    ref: deviceSettingsRef = None
    vpnHubs: List(DeviceSettingsVpnHub) = field(default_factory=list)


@dataclass
class DeviceSettingsVpn:
    """Device Settings - VPN"""
    enabled: bool = None
    edgeToDataCenter: bool = None
    ref: deviceSettingsRef = None
    isolationGroupId: str = None
    edgeToEdgeHub: EdgeToEdgeHub = None
    edgeToEdge: bool = None
    edgeToEdgeDetail: EdgeToEdgeDetail = None
    conditionalBackhaul: bool = None
    backHaulEdges: List(DeviceSettingsVpnHub) = field(default_factory=list)

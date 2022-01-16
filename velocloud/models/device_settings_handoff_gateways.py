from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_handoff_gateway import DeviceSettingsHandoffGateway
from velocloud.models.logicalid_reference import LogicalIdReference


@dataclass
class DeviceSettingsHandoffGateways:
    """Device Settings - Handoff Gateways"""
    override: bool = None
    autoSelect: bool = None
    gatewayList: List(DeviceSettingsHandoffGateway) = field(default_factory=list)
    gateways: List(LogicalIdReference) = field(default_factory=list)

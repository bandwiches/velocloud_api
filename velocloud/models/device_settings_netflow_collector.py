from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_netflow_filter_list import DeviceSettingsNetflowFilterList


@dataclass
class DeviceSettingsNetflowCollector:
    """Device Settings - Netflow Collector"""
    type: str = None
    sourceInterface: str = None
    name: str = None
    allowAllSegment: bool = None
    logicalId: str = None
    filterList: List(DeviceSettingsNetflowFilterList) = field(default_factory=list)

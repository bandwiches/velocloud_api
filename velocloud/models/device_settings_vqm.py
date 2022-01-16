from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_vqm_collector import DeviceSettingsVqmCollector
from velocloud.models.enums import deviceSettingsVqmProtocol


@dataclass
class DeviceSettingsVqm:
    """Device Settings - VQM"""
    enabled: bool = None
    override: bool = None
    protocol: deviceSettingsVqmProtocol = None
    collectors: List(DeviceSettingsVqmCollector) = field(default_factory=list)

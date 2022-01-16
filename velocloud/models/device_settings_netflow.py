from dataclasses import dataclass, field
from typing import List

from velocloud.models.device_settings_netflow_collector import DeviceSettingsNetflowCollector


@dataclass
class Interval:
    """Interval
    This is a custom class.
    """
    flowStats: int = None
    flowLinkStats: int = None
    tunnelStats: int = None
    vrfTable: int = None
    applicationTable: int = None
    interfaceTable: int = None
    linkTable: int = None


@dataclass
class DeviceSettingsNetflow:
    """Device Settings - Netflow"""
    enabled: bool = None
    override: bool = None
    collectors: List(DeviceSettingsNetflowCollector) = field(default_factory=list)
    version: int = None
    intervals: Interval = None

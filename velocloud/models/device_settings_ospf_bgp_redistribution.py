from dataclasses import dataclass

from velocloud.models.enums import deviceSettingsOspfBgpRouteRedistributionType


@dataclass
class DeviceSettingsOspfBgpRedistribution:
    """Device Settings - OSPF BGP Redistribution"""
    enabled: bool = None
    metric: int = None
    metricType: deviceSettingsOspfBgpRouteRedistributionType = None

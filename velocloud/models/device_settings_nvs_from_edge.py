from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_nvs_from_edge_site import DeviceSettingsNvsFromEdgeSite
from velocloud.models.enums import deviceSettingsRef


@dataclass
class Config:
    """Config
    This is a custom class.
    """
    useAllPublicWanLinks: bool = None
    enabled: bool = None


@dataclass
class Providers:
    """Providers
    This is a custom class.
    """
    logicalId: str = None
    config: Config = None
    sites: List(DeviceSettingsNvsFromEdgeSite) = field(default_factory=list)


@dataclass
class Provider:
    """Provider
    This is a custom class.
    """
    ref: deviceSettingsRef = None


@dataclass
class DeviceSettingsNvsFromEdge:
    """Device SEttings NVS From Edge"""
    enabled: bool = None
    override: bool = None
    provider: Provider = None
    providers: List(Providers) = field(default_factory=list)

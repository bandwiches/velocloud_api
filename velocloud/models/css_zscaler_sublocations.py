from dataclasses import dataclass, field
from typing import List
from velocloud.models.enums import gwDisplayTimeUnit


@dataclass
class GwProperties:
    """Gateway Properties
    This is a custom class.
    """
    sslScanEnabled: bool = None
    authRequired: bool = None
    surrogateIP: bool = None
    idleTimeInMinutes: int = None
    displayTimeUnit: gwDisplayTimeUnit = None
    surrogateIPEnforcedForKnownBrowsers: bool = None
    surrogateRefreshTimeInMinutes: int = None
    surrogateRefreshTimeUnit: gwDisplayTimeUnit = None
    dnBandwidth: int = None
    upBandwidth: int = None


@dataclass
class CssZscalerSubLocations:
    """CSS - Zscaler - Sub Locations"""
    internalId: str = None
    name: str = None
    ruleId: str = None
    gwProperties: GwProperties = None
    vlans: List(int) = field(default_factory=list)
    includeAllVlans: bool = None
    includeAllLanInterfaces: bool = None
    lanRoutedInterfaces: List(str) = field(default_factory=list)
    ipAddressSelectionManual: bool = None
    ipAddresses: List(str) = field(default_factory=list)  # Should be IPv4Address type?

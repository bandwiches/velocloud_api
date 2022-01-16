from dataclasses import dataclass, field
from typing import List


@dataclass
class DhcpOptionMetadata:
    """DHCP Option Metadata
    This is a custom class.
    """
    dataType: str = None
    description: str = None
    display: bool = None
    list: bool = None
    name: str = None
    option: int = None


@dataclass
class DhcpOption:
    """DHCP Option
    This is a custom class.
    """
    option: int = None
    value: str = None
    type: str = None
    metaData: DhcpOptionMetadata = None


@dataclass
class DhcpRelay:
    """DHCP Relay
    This is a custom class.
    """
    servers: List(str) = field(default_factory=list)
    sourceFromSecondaryIp: bool = None


@dataclass
class EdgeDeviceSettingsDataDhcpServer:
    """Edge Device Settings Data DHCP Server"""
    baseDhcpAddr: int = None
    enabled: bool = None
    leaseTimeSeconds: int = None
    dhcpRelay: DhcpRelay = None
    numDhcpAddr: int = None
    staticReserved: int = None
    options: List(DhcpOption) = field(default_factory=list)

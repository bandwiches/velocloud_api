from dataclasses import dataclass


@dataclass
class Metadata:
    """Device Settings DHCP Option Metadata
    This is a custom class.
    """
    dataType: str = None
    description: str = None
    display: bool = None
    list: bool = None
    name: str = None
    option: int = None


@dataclass
class DeviceSettingsDhcpOption:
    """Device Settings DHCP Option"""
    option: int = None
    value: str = None
    type: str = None
    metaData: Metadata = None

from dataclasses import dataclass, field
from typing import List
from velocloud.models.enums import interfaceDuplex, lanInterfaceAuthenticationType, lanInterfaceMode, lanInterfaceSecurityMode, lanInterfaceType


@dataclass
class Layer2:
    """Layer 2
    This is a custom class.
    """
    autonegotiation: bool = None
    speed: str = None
    duplex: interfaceDuplex = None
    MTU: int = None


@dataclass
class DeviceSettingsLanInterface:
    """Device Settings LAN Interface"""
    override: bool = None
    name: str = None
    cwp: bool = None
    disabled: bool = None
    l2: Layer2 = None
    portMode: lanInterfaceMode = None
    space: str = None
    type: lanInterfaceType = None
    untaggedVlan: str = None
    vlanIds: List(int) = field(default_factory=list)
    authenticationType: lanInterfaceAuthenticationType = None  # This probably fails
    broadcastSsid: bool = None
    passphrase: str = None
    ssid: str = None
    securityMode: lanInterfaceSecurityMode = None

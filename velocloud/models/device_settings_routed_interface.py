from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_routed_interface_addressing import DeviceSettingsRoutedInterfaceAddressing
from velocloud.models.device_settings_routed_interface_dsl_settings import DeviceSettingsRoutedInterfaceDslSettings
from velocloud.models.device_settings_routed_interface_l2 import DeviceSettingsRoutedInterfaceL2
from velocloud.models.device_settings_routed_interface_ospf import DeviceSettingsRoutedInterfaceOspf
from velocloud.models.device_settings_subinterface import DeviceSettingsSubinterface
from velocloud.models.enums import cellularNetwork, deviceSettingsWanOverlay, dslMode, igmpType, pimType, rPF
from velocloud.models.device_settings_dhcp import DeviceSettingsDhcp


@dataclass
class MacBypass:
    """MAC Bypass
    This is a custom class.
    """
    address: str = None
    description: str = None


@dataclass
class RadiusAuthentication:
    """RADIUS Authentication
    This is a custom class.
    """
    enabled: bool = None
    macBypass: List(MacBypass) = field(default_factory=list)


@dataclass
class Pim:
    """PIM
    This is a custom class.
    """
    enable: bool = None
    type: pimType = None


@dataclass
class Igmp:
    """IGMP
    This is a custom class.
    """
    enabled: bool = None
    type: igmpType = None


@dataclass
class Multicast:
    """Multicast
    This is a custom class.
    """
    igmp: Igmp = None
    igmpHostQueryIntervalSeconds: int = None
    igmpMaxQueryResponse: int = None
    pim: Pim = None
    pimKeepAliveTimerSeconds: int = None
    pimPruneIntervalSeconds: int = None
    pimHelloTimerSeconds: int = None


@dataclass
class DslSettings:
    """DSL Settings
    This is a custom class.
    """
    mode: dslMode = None
    properties: DeviceSettingsRoutedInterfaceDslSettings = None


@dataclass
class Cellular:
    """Cellular
    This is a custom class.
    """
    simPin: str = None
    network: cellularNetwork = None
    apn: str = None
    username: str = None
    password: str = None


@dataclass
class DeviceSettingsRoutedInterface:
    """Device Settings Routed Interface"""
    override: bool = None
    disabled: bool = None
    addressing: DeviceSettingsRoutedInterfaceAddressing = None
    advertise: bool = None
    cellular: Cellular = None
    dhcpServer: DeviceSettingsDhcp = None
    dslSettings: DslSettings = None
    encryptOverlay: bool = None
    l2: DeviceSettingsRoutedInterfaceL2 = None
    multicast: Multicast = None
    name: str = None
    natDirect: bool = None
    ospf: DeviceSettingsRoutedInterfaceOspf = None
    pingResponse: bool = True  # API has default value
    radiusAuthentication: RadiusAuthentication = None
    segmentId: int = None
    sfpType: dslMode = None  # I think the API is wrong here if this is fiber related
    subinterfaces: List(DeviceSettingsSubinterface) = field(default_factory=list)
    rpf: rPF = None
    trusted: bool = None
    underlayAccounting: bool = True  # API has default value
    vlanId: int = None
    wanOverlay: deviceSettingsWanOverlay = None

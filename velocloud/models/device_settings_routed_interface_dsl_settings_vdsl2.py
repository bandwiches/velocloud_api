from dataclasses import dataclass

from velocloud.models.enums import deviceSettingsRoutedInterfaceVsdl2Profile


@dataclass
class DeviceSettingsRoutedInterfaceDslSettingsVdsl2:
    """Device Settings - Routed Interface DSL Settings VDSL2"""
    profile: deviceSettingsRoutedInterfaceVsdl2Profile = None

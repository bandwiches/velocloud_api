from dataclasses import dataclass


@dataclass
class DeviceSettingsVpnProfileIsolationDeprecated:
    """Device Settings - VPN Profile Isolation (Deprecated)"""
    enabled: bool = None
    profileLogicalId: str = None
    isolateDynamic: bool = None

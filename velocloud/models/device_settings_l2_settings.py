from dataclasses import dataclass


@dataclass
class DeviceSettingsL2Settings:
    """Device Settings - L2 Settings"""
    overrideARPTimeout: bool = None
    arpStaleTimeoutMinute: int = None
    arpDeadTimeoutMinutes: int = None
    arpCleanupTimeoutMinutes: int = None

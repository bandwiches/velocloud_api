from dataclasses import dataclass


@dataclass
class DeviceSettingsAnalyticsSettings:
    """Device Settings - Analytics Settings"""
    analyticsEnabled: bool
    sourceInterface: str
    override: bool = None

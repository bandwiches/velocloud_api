from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_ntp_server import DeviceSettingsNtpServer


@dataclass
class DeviceSettingsNtp:
    """Device Settings NTP"""
    sourceInterface: str = None
    enabled: bool = None
    override: bool = None
    servers: List(DeviceSettingsNtpServer) = field(default_factory=list)

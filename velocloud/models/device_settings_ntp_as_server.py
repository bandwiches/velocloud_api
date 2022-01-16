from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_ntp_key import DeviceSettingsNtpKey
from velocloud.models.enums import deviceSettingsNtpAuth


@dataclass
class DeviceSettingsNtpAsServer:
    """Device Settings NTP As Server"""
    enabled: bool = None
    override: bool = None
    authentication: deviceSettingsNtpAuth = None
    keys: List(DeviceSettingsNtpKey) = field(default_factory=list)

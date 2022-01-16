from dataclasses import dataclass


@dataclass
class DeviceSettingsNtpServer:
    """Device Settings NTP Server"""
    server: str = None

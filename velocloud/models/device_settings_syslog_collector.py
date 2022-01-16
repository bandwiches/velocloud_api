from dataclasses import dataclass
from typing import List
from velocloud.models.enums import deviceSettingsSyslogCollectorIpProtocol, deviceSettingsSyslogCollectorRole, deviceSettingsSyslogCollectorSeverity


@dataclass
class DeviceSettingsSyslogCollector:
    """Device Settings - Syslog Collector"""
    host: str
    port: int
    protocol: deviceSettingsSyslogCollectorIpProtocol
    roles: List(deviceSettingsSyslogCollectorRole)
    severity: deviceSettingsSyslogCollectorSeverity
    sourceInterface: str
    tag: str = None

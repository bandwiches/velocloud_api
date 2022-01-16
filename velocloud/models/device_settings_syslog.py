from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_syslog_collector import DeviceSettingsSyslogCollector
from velocloud.models.enums import deviceSettingsSyslogFacilityCode


@dataclass
class DeviceSettingsSyslog:
    """Device Settings - Syslog"""
    enabled: bool
    collectors: List() = field(default_factory=list)
    facilityCode: deviceSettingsSyslogFacilityCode = None
    override: bool = None
    collectors: List(DeviceSettingsSyslogCollector) = field(default_factory=list)

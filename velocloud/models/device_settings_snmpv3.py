from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_snmpv3_user import DeviceSettingsSnmpv3User


@dataclass
class DeviceSettingsSnmpv3:
    """Device Settings - SNMP v3"""
    enabled: bool = None
    users: List(DeviceSettingsSnmpv3User) = field(default_factory=list)

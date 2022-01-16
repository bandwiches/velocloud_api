from dataclasses import dataclass
from velocloud.models.device_settings_snmpv2c import DeviceSettingsSnmpv2c
from velocloud.models.device_settings_snmpv3 import DeviceSettingsSnmpv3


@dataclass
class DeviceSettingsSnmp:
    """Device Settings - SNMP"""
    override: bool = None
    port: int = None
    snmpv2c: DeviceSettingsSnmpv2c = None
    snmpv3: DeviceSettingsSnmpv3 = None

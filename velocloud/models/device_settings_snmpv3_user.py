from dataclasses import dataclass


@dataclass
class DeviceSettingsSnmpv3User:
    """Device Settings - SNMP v3 User"""
    name: str = None
    passphrase: str = None
    authAlg: str = None
    privacy: bool = None
    encrAlg: str = None

from dataclasses import dataclass


@dataclass
class DeviceSettingsOspfArea:
    """Device Settings - OSPF Area"""
    id: int = None
    name: str = None
    type: str = None

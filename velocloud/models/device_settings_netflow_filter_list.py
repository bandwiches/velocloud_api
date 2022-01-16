from dataclasses import dataclass


@dataclass
class DeviceSettingsNetflowFilterList:
    """Device Settings - Netflow Filter List"""
    type: str = None
    name: str = None
    logicalId: str = None

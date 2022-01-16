from dataclasses import dataclass


@dataclass
class DeviceSettingsVqmCollector:
    """Device Settings - VQM Collector"""
    address: str = None
    port: int = None

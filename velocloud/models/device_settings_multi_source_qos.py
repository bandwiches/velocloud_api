from dataclasses import dataclass


@dataclass
class DeviceSettingsMultiSourceQos:
    """Devide Settings Mutli-Source QoS"""
    enabled: bool = None
    override: bool = None
    highRatio: int = None
    normalRatio: int = None
    lowRatio: int = None
    maxCapThreshold: int = None
    minCapThreshold: int = None

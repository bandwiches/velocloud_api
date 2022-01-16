from dataclasses import dataclass


@dataclass
class DeviceSettings:
    """Back Haul Edge
    This is a custom class.
    """
    backHaulEdge: dict = None
    dataCenter: dict = None


@dataclass
class QosRefs:
    """QoS Refs"""
    deviceSettings: DeviceSettings

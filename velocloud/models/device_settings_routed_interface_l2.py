from dataclasses import dataclass

from velocloud.models.enums import interfaceDuplex


@dataclass
class DeviceSettingsRoutedInterfaceL2:
    """Device Settings Routed Interface L2"""
    autonegotiation: bool = None
    speed: str = None
    duplex: interfaceDuplex = None
    MTU: int = None

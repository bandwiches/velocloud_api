from dataclasses import dataclass


@dataclass
class DeviceSettingsroutedInterfaceDslSettingsAdsl2:
    """Dveice Settings - Routed Interface DSL Settings ADSL2"""
    pvc: int = None
    vpi: int = None  # 0 - 255
    vci: int = None  # 35 - 65535
    vlan: int = None

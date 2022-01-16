from dataclasses import dataclass


@dataclass
class DeviceSettingsBgpOspfRedistribution:
    """Device Settings BGP OSPF Redistribution"""
    enabled: bool = None
    metric: int = None

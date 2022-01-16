from dataclasses import dataclass


@dataclass
class DeviceSettingsBfdRule:
    """Device Settings BFD Rule"""
    peerAddress: str = None
    localAddress: str = None
    multihop: bool = None
    detectMultiplier: int = None
    receiveInterval: int = None
    transmitInterval: int = None

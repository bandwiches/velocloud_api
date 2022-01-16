from dataclasses import dataclass
from ipaddress import IPv4Address


@dataclass
class DeviceSettingsNatDualRule:
    """Device Settings - NAT Dual Rule"""
    srcInsideCidrIp: IPv4Address
    srcInsideCidrPrefix: int
    srcInsideCidrNetmask: IPv4Address
    srcOutsideCidrIp: IPv4Address
    srcOutsideCidrPrefix: int
    srcOutsideCidrNetmask: IPv4Address
    destInsideCidrIp: IPv4Address
    destInsideCidrPrefix: int
    destInsideCidrNetmask: IPv4Address
    destOutsideCidrIp: IPv4Address
    destOutsideCidrPrefix: int
    destOutsideCidrNetmask: IPv4Address
    description: str = None

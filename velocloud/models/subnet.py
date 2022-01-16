from dataclasses import dataclass


@dataclass
class Subnet:
    """Subnet"""
    cidrIp: str = None
    cidrPrefix: int = None

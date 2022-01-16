from dataclasses import dataclass
from datetime import datetime
from ipaddress import IPv4Address


@dataclass
class ClientDevice:
    """Client Device"""
    id: int
    created: datetime  # datetime
    enterpriseId: int
    macAddress: str
    hostName: str
    ipAddress: IPv4Address
    os: int
    osName: str
    osVersion: str
    deviceType: str
    deviceModel: str
    lastContact: datetime  # datetime
    modified: datetime  # datetime

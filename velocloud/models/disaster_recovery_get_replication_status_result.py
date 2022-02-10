from dataclasses import dataclass, field
from datetime import datetime
from ipaddress import IPv4Address
from typing import List
from velocloud.models.enums import disasterRecoveryRole, disasterRecoveryState


@dataclass
class StateHistory:
    """State History
    This is a custom class.
    """
    _from: disasterRecoveryState = None
    to: disasterRecoveryState = None
    timestamp: datetime = None  # datetime

    @property
    def from_state(self):
        return self._from


@dataclass
class ClientCount:
    """Client Count
    This is a custom class.
    """
    edgeCount: int = None
    gatewayCount: int = None
    currentActiveEdgeCount: int = None
    currentActiveEdgeCount: int = None
    currentActiveGatewayCount: int = None
    currentStandbyGatewayCount: int = None


@dataclass
class Standby:
    """Standby
    This is a custom class.
    """
    standbyAddress: IPv4Address = None
    standbyReplicationAddress: IPv4Address = None
    standbyUuid: str = None


@dataclass
class DisasterRecoveryGetReplicationStatusResult:
    """Disaster Recovery Get Replication Status Result"""
    activeAddress: IPv4Address
    drState: disasterRecoveryState
    drVCOUser: str
    failureDescription: str
    role: disasterRecoveryRole
    roleTimestamp: datetime  # datetime
    standbyList: List(Standby)
    vcoIp: IPv4Address
    vcoUuid: str
    activeReplicationAddress: str = None
    clientContact: List() = field(default_factory=list)
    clientCount: ClientCount = None
    lastDrProtectedTime: datetime = None  # datetime
    stateHistory: List(StateHistory) = field(default_factory=list)
    stateTimestamp: datetime = None  # datetime
    vcoReplicationIp: IPv4Address = None

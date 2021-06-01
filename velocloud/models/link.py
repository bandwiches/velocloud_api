from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List


class NetworkSide(Enum):
    """Network Side (v4.2.1)"""
    UNKNOWN = "UNKNOWN"
    UNKOWN = "UNKOWN"  # API Typo
    WAN = "WAN"
    LAN = "LAN"


class NetworkType(Enum):
    """Network Type (v4.2.1)"""
    UNKNOWN = "UNKNOWN"
    WIRELESS = "WIRELESS"
    ETHERNET = "ETHERNET"
    WIFI = "WIFI"


class State(Enum):
    """Link State (v4.2.1)"""
    UNKNOWN = "UNKNOWN"
    STABLE = "STABLE"
    UNSTABLE = "UNSTABLE"
    DISCONNECTED = "DISCONNECTED"
    QUIET = "QUIET"
    INITIAL = "INITIAL"
    STANDBY = "STANDBY"


class BackupState(Enum):
    """Backup State (v4.2.1)"""
    UNCONFIGURED = "UNCONFIGURED"
    STANDBY = "STANDBY"
    ACTIVE = "ACTIVE"


class LinkMode(Enum):
    """Link Mode (v4.2.1)"""
    ACTIVE = "ACTIVE"
    BACKUP = "BACKUP"
    HOSTSTASNDBY = "HOSTSTANDBY"


class ServiceState(Enum):
    """Service State (v4.2.1)"""
    IN_SERVICE = "IN_SERVICE"
    OUT_OF_SERVICE = "OUT_OF_SERVICE"
    PENDING_SERVICE = "PENDING_SERVICE"


class ServiceGroups(Enum):
    """Service Groups (v4.2.1)"""
    ALL = "ALL"
    PRIVATE_WIRED = "PRIVATE_WIRED"
    PUBLIC_WIRED = "PUBLIC_WIRED"
    PUBLIC_WIRELESS = "PUBLIC_WIRELESS"


@dataclass
class Link:
    id: int
    created: datetime
    edgeId: int
    logicalId: str
    internalId: str
    interface: str
    macAddress: str
    ipAddress: str
    netmask: str
    networkSide: NetworkSide
    networkType: NetworkType
    displayName: str
    isp: str
    org: str
    lat: float
    lon: float
    lastActive: datetime
    state: State
    backupState: BackupState
    # vpnState: None  # Depracated
    lastEvent: datetime
    lastEventState: State
    alertsEnabled: int
    operatorAlertsEnabled: int
    serviceState: ServiceState
    modified: datetime
    linkMode: LinkMode = None
    serviceGroups: List[ServiceGroups] = field(default_factory=list)

    def __repr__(self):
        return str(type(self))

    @classmethod
    def from_dict(cls, profile: dict):
        """Edge Link Factory"""
        created = None
        lastActive = None
        lastEvent = None
        modified = None

        # Datetimes
        try:
            created = datetime.strptime(profile["created"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            lastActive = datetime.strptime(profile["lastActive"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            lastEvent = datetime.strptime(profile["lastEvent"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            modified = datetime.strptime(profile["modified"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass

        return cls(
            id=profile.get("id"),
            created=created,
            edgeId=profile.get("edgeId"),
            logicalId=profile.get("logicalId"),
            internalId=profile.get("internalId"),
            interface=profile.get("interface"),
            macAddress=profile.get("macAddress"),
            ipAddress=profile.get("ipAddress"),
            netmask=profile.get("netmask"),
            networkSide=NetworkSide(profile.get('networkSide')),
            networkType=NetworkType(profile.get('networkType')),
            displayName=profile.get("displayName"),
            isp=profile.get("isp"),
            org=profile.get("org"),
            lat=profile.get("lat"),
            lon=profile.get("lon"),
            lastActive=lastActive,
            state=State(profile.get('state')),
            backupState=BackupState(profile.get('backupState')),
            linkMode=LinkMode(profile.get('linkMode')),
            # vpnState=profile.get("vpnState"),  # Depracated
            lastEvent=lastEvent,
            lastEventState=State(profile.get('lastEventState')),
            alertsEnabled=profile.get("alertsEnabled"),
            operatorAlertsEnabled=profile.get("operatorAlertsEnabled"),
            serviceState=ServiceState(profile.get('serviceState')),
            modified=modified,
            serviceGroups=profile.get("serviceGroups")
        )

from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from velocloud.models.enums import linkBackupState, linkLinkMode, linkNetworkSide, linkNetworkType, linkState, tinyint, linkServiceState, linkServiceGroups


@dataclass
class Link:
    """Link"""
    id: int
    created: datetime  # datetime
    edgeId: int
    logicalId: str
    internalId: str
    interface: str
    macAddress: str
    ipAddress: str
    netmask: str
    networkSide: linkNetworkSide
    networkType: linkNetworkType
    displayName: str
    isp: str
    org: str
    lat: float
    lon: float
    lastActive: datetime
    state: linkState
    backupState: linkBackupState
    # vpnState: None  # Depracated
    lastEvent: datetime
    lastEventState: linkState
    alertsEnabled: tinyint
    operatorAlertsEnabled: tinyint
    serviceState: linkServiceState
    modified: datetime
    linkMode: linkLinkMode = None
    serviceGroups: List[linkServiceGroups] = field(default_factory=list)

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
            networkSide=linkNetworkSide(profile.get('networkSide')),
            networkType=linkNetworkType(profile.get('networkType')),
            displayName=profile.get("displayName"),
            isp=profile.get("isp"),
            org=profile.get("org"),
            lat=profile.get("lat"),
            lon=profile.get("lon"),
            lastActive=lastActive,
            state=linkState(profile.get('state')),
            backupState=linkBackupState(profile.get('backupState')),
            linkMode=linkLinkMode(profile.get('linkMode')),
            # vpnState=profile.get("vpnState"),  # Depracated
            lastEvent=lastEvent,
            lastEventState=linkState(profile.get('lastEventState')),
            alertsEnabled=profile.get("alertsEnabled"),
            operatorAlertsEnabled=profile.get("operatorAlertsEnabled"),
            serviceState=linkServiceState(profile.get('serviceState')),
            modified=modified,
            serviceGroups=profile.get("serviceGroups")
        )

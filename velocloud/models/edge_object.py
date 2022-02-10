from dataclasses import dataclass
from velocloud.models.enums import edgeActivationState, edgeHaState, edgeServiceState, edgeState as eS, endpointPkiMode as ePM, tinyint


@dataclass
class EdgeObject:
    """Edge Object"""
    activationKey: str = None
    activationKeyExpires: str = None
    activationState: edgeActivationState = None
    activationTime: str = None
    alertsEnabled: tinyint = None
    buildNumber: str = None
    created: str = None
    customInfo: str = None
    description: str = None
    deviceFamily: str = None
    deviceId: str = None
    dnsName: str = None
    edgeState: eS = None
    edgeStateTime: str = None
    endpointPkiMode: ePM = None
    enterpriseId: int = None
    factorySoftwareVersion: str = None
    factoryBuildNumber: str = None
    haLastContact: str = None
    haPreviousState: edgeHaState = None
    haSerialNumber: str = None
    haState: edgeHaState = None
    id: int = None
    isLive: int = None
    lastContact: str = None
    logicalId: str = None
    modelNumber: str = None
    modified: str = None
    name: str = None
    operatorAlertsEnabled: tinyint = None
    selfMacAddress: str = None
    serialNumber: str = None
    serviceState: edgeServiceState = None
    serviceUpSince: str = None
    siteId: int = None
    softwareUpdated: str = None
    softwareVersion: str = None
    systemUpSince: str = None

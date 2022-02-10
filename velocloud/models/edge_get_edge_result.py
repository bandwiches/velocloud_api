from dataclasses import dataclass
from typing import List
from velocloud.models.enums import edgeActivationState, edgeHaState, edgeServiceState, edgeState, endpointPkiMode, tinyint
from velocloud.models.model_configuration import ModelConfiguration
from velocloud.models.enterprise import Enterprise
from velocloud.models.link import Link
from velocloud.models.site import Site


@dataclass
class EdgeGetEdgeResult:
    """Edge Get Edge Result"""
    activationKey: str
    activationKeyExpires: str
    activationState: edgeActivationState
    activationTime: str
    alertsEnabled: tinyint
    buildNumber: str
    created: str
    customInfo: str
    description: str
    deviceFamily: str
    deviceId: str
    dnsName: str
    edgeState: edgeState
    edgeStateTime: str
    endpointPkiMode: endpointPkiMode
    enterpriseId: int
    haLastContact: str
    haPreviousState: edgeHaState
    haSerialNumber: str
    haState: edgeHaState
    id: int
    isLive: int
    lastContact: str
    logicalId: str
    modelNumber: str
    modified: str
    name: str
    operatorAlertsEnabled: tinyint
    selfMacAddress: str
    serialNumber: str
    serviceState: edgeServiceState
    serviceUpSince: str
    siteId: int
    softwareUpdated: str
    softwareVersion: str
    systemUpSince: str
    configuration: ModelConfiguration
    enterprise: Enterprise
    links: List(Link)
    recentLinks: List(Link)
    site: Site
    factorySoftwareVersion: str = None
    factoryBuildNumber: str = None

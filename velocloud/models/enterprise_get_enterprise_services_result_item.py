from dataclasses import dataclass, field
from typing import List
from datetime import datetime
from velocloud.models.enums import tinyint


@dataclass
class EdgeQosUsage:
    """Edge QoS Usage
    This is a custom class.
    """
    segmentObjectId: int = None
    edgeId: int = None
    name: str = None
    logicalId: str = None
    profileId: int = None


@dataclass
class EnterpriseGetEnterpriseServicesResultItem:
    """Enterprise Get Enterprise Services Result Item"""
    id: int
    created: datetime
    operatorId: int
    networkId: int
    enterpriseId: int
    edgeId: int
    gatewayId: int
    gatewayId: int
    description: str
    object: str
    name: str
    type: str
    logicalId: str
    alertsEnabled: tinyint
    operatorAlertsEnabled: tinyint
    status: str
    statusModified: datetime
    previousData: dict
    previousCreated: datetime
    draftData: str
    draftCreated: datetime
    draftComment: str
    data: dict
    lastContact: datetime
    version: str
    modified: datetime
    profileCount: int = None
    edgeCount: int = None
    groupCount: int = None
    edgeQOSUsage: List(EdgeQosUsage) = field(default_factory=list)

from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import edgeState, edgeActivationState


@dataclass
class ProxyEdgeInventoryObject:
    """Proxy Edge Inventory Object"""
    enterpriseName: str
    enterpriseId: int
    edgeName: str
    edgeId: int
    created: datetime
    edgeState: edgeState
    serialNumber: str
    haSerialNumber: str
    activationState: edgeActivationState
    activationTime: datetime
    modelNumber: str
    softwareVersion: str
    softwareVersion: datetime
    lastContact: datetime

from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import edgeActivationState, edgeState


@dataclass
class EnterpriseProxyGetEnterpriseProxyEdgeInventoryResultItem:
    """Enterprise Proxy Get Enterprise Proxy Edge Inventory Result Item"""
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
    softwareUpdated: datetime
    lastContact: datetime

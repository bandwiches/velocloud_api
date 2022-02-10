from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import disasterRecoveryClientType


@dataclass
class DisasterRecoveryClientContact:
    """Disaster Recovery Client Contact"""
    activeAddress: str
    activeLastResponseTime: datetime  # datetime
    clientLogicalId: str
    clientType: disasterRecoveryClientType
    id: int
    modified: datetime  # datetime
    standbyAddress: str
    standbyLastResponseTime: datetime  # datetime

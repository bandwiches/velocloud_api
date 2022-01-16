from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import eventBaseCategory, eventBaseSeverity


@dataclass
class AggregateEnterpriseEvent:
    """Aggregate Enterprise Event"""
    id: int
    eventTime: datetime  # datetime
    event: str
    category: eventBaseCategory
    severity: eventBaseSeverity
    message: str
    enterpriseId: int
    enterpriseName: str
    enterpriseUsername: str
    edgeName: str
    detail: str = None

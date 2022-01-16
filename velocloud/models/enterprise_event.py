from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import eventBaseCategory, eventBaseSeverity


@dataclass
class EnterpriseEvent:
    """Enterprise Event"""
    id: int
    eventTime: datetime  # datetime
    event: str
    category: eventBaseCategory
    severity: eventBaseSeverity
    message: str
    detail: str
    enterpriseUsername: str
    edgeName: str

from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import eventBaseCategory, eventBaseSeverity


@dataclass
class EventBase:
    """Event Base"""
    id: int = None
    eventTime: datetime = None  # datetime
    event: str = None
    category: eventBaseCategory = None
    severity: eventBaseSeverity = None
    message: str = None

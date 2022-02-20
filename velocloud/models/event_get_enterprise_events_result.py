from dataclasses import dataclass
from typing import List
from velocloud.models.enterprise_event import EnterpriseEvent
from velocloud.models.list_metadata import ListMetadata


@dataclass
class EventGetEnterpriseEventsResult:
    """Event Get Enterprise Events Result"""
    data: List(EnterpriseEvent)
    metaData: ListMetadata

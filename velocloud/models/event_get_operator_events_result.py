from dataclasses import dataclass
from typing import List
from velocloud.models.operator_event import OperatorEvent
from velocloud.models.list_metadata import ListMetadata


@dataclass
class EventGetOperatorEventsResult:
    """Event Get Operator Events Result"""
    data: List(OperatorEvent)
    metaData: ListMetadata

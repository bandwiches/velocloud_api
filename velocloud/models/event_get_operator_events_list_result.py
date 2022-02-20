from dataclasses import dataclass, field
from typing import List
from velocloud.models.operator_event import OperatorEvent
from velocloud.models.list_metadata import ListMetadata
from velocloud.models.count_result import CountResult


@dataclass
class EventGetOperatorEventsListResult:
    """Event Get Operator Events List Result"""
    data: List(OperatorEvent) = field(default_factory=list)
    metaData: ListMetadata = None
    count: CountResult = None

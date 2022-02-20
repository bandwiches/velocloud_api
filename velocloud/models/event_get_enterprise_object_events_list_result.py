from dataclasses import dataclass, field
from typing import List
from velocloud.models.enterprise_event import EnterpriseEvent
from velocloud.models.list_metadata import ListMetadata
from velocloud.models.count_result import CountResult


@dataclass
class EventGetEnterpriseObjectEventsListResult:
    """Event Get Enterprise Object Events List Result"""
    data: List(EnterpriseEvent) = field(default_factory=list)
    metaData: ListMetadata = None
    count: CountResult = None

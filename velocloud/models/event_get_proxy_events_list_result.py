from dataclasses import dataclass, field
from typing import List
from velocloud.models.proxy_event import ProxyEvent
from velocloud.models.list_metadata import ListMetadata
from velocloud.models.count_result import CountResult


@dataclass
class EventGetProxyEventsListResult:
    """Event Get Proxy Events List Result"""
    data: List(ProxyEvent) = field(default_factory=list)
    metaData: ListMetadata = None
    count: CountResult = None

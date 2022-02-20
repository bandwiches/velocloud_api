from dataclasses import dataclass
from typing import List
from velocloud.models.proxy_event import ProxyEvent
from velocloud.models.list_metadata import ListMetadata


@dataclass
class EventGetProxyEventsResult:
    """Event Get Proxy Events Result"""
    data: List(ProxyEvent)
    metaData: ListMetadata

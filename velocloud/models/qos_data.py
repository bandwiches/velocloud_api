from dataclasses import dataclass
from typing import List
from velocloud.models.qos_segments import QosSegments


@dataclass
class ServiceRateLimit:
    """QOS Service Rate Limit
    This is a custom class.
    """
    enabled: bool
    inputType: str = None
    value: int = None


@dataclass
class QosData:
    """QOS Data"""
    segments: List(QosSegments)
    serviceRateLimit: ServiceRateLimit = None

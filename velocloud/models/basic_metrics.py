from dataclasses import dataclass, field
from typing import List
from velocloud.models.enums import basicMetric


@dataclass
class BasicMetrics:
    """Basic Metrics"""
    basic_metrics: List(basicMetric) = field(default_factory=list)

from dataclasses import dataclass, field
from typing import List
from velocloud.models.metric_filter import MetricFilter


@dataclass
class MetricFilters:
    """Metric Filters"""
    data: List(MetricFilter) = field(default_factory=list)

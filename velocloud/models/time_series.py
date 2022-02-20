from dataclasses import dataclass
from datetime import datetime
from typing import List
from velocloud.models.enums import timeSeriesMetric
from velocloud.models.time_series_distribution import TimeSeriesDistribution


@dataclass
class TimeSeries:
    """Time Series"""
    data: List(int)
    max: int
    metric: timeSeriesMetric
    min: int
    startTime: datetime
    tickInterval: int
    total: int
    average: int = None
    median: int = None
    distribution: TimeSeriesDistribution = None

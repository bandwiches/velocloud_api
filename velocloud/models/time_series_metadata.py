from dataclasses import dataclass
from typing import List
from velocloud.models.time_series import TimeSeries


@dataclass
class TimeSeriesMetadata:
    """Time Series Metadata"""
    series: List(TimeSeries)

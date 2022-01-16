from dataclasses import dataclass
from typing import List
from velocloud.models.link_quality_object_distribution import LinkQualityObjectDistribution
from velocloud.models.enums import linkMetricTrafficType, linkMetricAction, linkMetricMetric, linkMetricState


@dataclass
class Score:
    """Score
    This is a custom class.
    """
    wildcard: int = None


@dataclass
class StateMapDataItem:
    """State Map Data Item
    This is a custom class.
    """
    before: int = None
    after: int = None
    action: int = None


@dataclass
class StateMapData:
    """State Map Data
    This is a custom class.
    """
    wildcard: StateMapDataItem


@dataclass
class StateMap:
    """State Map
    This is a custom class.
    """
    wildcard: StateMapData


@dataclass
class Metrics:
    """Metrics
    This is a custom class.
    """
    trafficType: linkMetricTrafficType
    action: linkMetricAction
    metric: linkMetricMetric
    beforeState: linkMetricState
    afterState: linkMetricState


@dataclass
class Detail:
    """Metadata Detail
    This is a custom class.
    """
    latencyMsRx: int = None
    latencyMsTx: int = None
    lossPctRx: int = None
    lossPctTx: int = None
    jitterMsRx: int = None
    jitterMsTx: int = None


@dataclass
class Metadata:
    """Metadata
    This is a custom class.
    """
    detail: Detail = None
    metrics: List(Metrics) = None
    stateMap: StateMap = None


@dataclass
class After:
    """After
    This is a custom class.
    """
    wildcard: int = None


@dataclass
class Before:
    """Before
    This is a custom class.
    """
    wildcard: int = None


@dataclass
class LinkQualityObjectTimeseriesData:
    """Link Quality Object Timeseries Data

    Not quite sure what all these wildcard things are about < * >
    """
    after: After
    metadata: Metadata
    timestamp: int
    before: Before = None
    distribution: LinkQualityObjectDistribution = None
    score: Score = None

from dataclasses import dataclass
from typing import List
from velocloud.models.link_quality_object_distribution import LinkQualityObjectDistribution
from velocloud.models.link_quality_object_timeseries_data import LinkQualityObjectTimeseriesData


@dataclass
class Score:
    """Score
    This is a custom class.

    Presents a summary QoE scores by traffic type, where:
        0: represents voice traffic
        1: represents video traffic
        2: represents transactional traffic
    """
    data: int = None


@dataclass
class LinkQualityObject:
    """Link Quality Object

    Args:
        distribution (LinkQualityObjectDistribution): Summarizes state distributions over the request interval by traffic type.
        sampleCount (int): The number of events sampled to compute QoE values over the request interval. The samples themselves appear in the timeseries list.
        sampleLength (int): The total number of link quality events reported by the Edge over the request interval.
        score (Score): Presents a summary QoE scores by traffic type, where the 0 key represents voice traffic, the 1 key represents video traffic, and the 2 key represent transactional traffic.
        timeseries ([LinkQualityObjectTimeseriesData]):
        totalScore (int):
    """
    distribution: LinkQualityObjectDistribution
    sampleCount: int
    samepleLength: int
    score: Score
    timeseries: List(LinkQualityObjectTimeseriesData)
    totalScore: int

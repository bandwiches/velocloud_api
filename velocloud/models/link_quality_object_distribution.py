from dataclasses import dataclass


@dataclass
class LinkQualityObjectDistribution:
    """Link Quality Object Distribution
    Summarizes state distributions over the request interval by traffic type.
    """
    wildcard: dict = None

from dataclasses import dataclass


@dataclass
class PathQualityStateDistribution:
    """Path Quality State Distribution"""
    OFFLINE: int = None
    UNKNOWN: int = None
    RED: int = None
    YELLOW: int = None
    GREEN: int = None

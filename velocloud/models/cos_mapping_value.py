from dataclasses import dataclass


@dataclass
class CosMappingValue:
    """CoS Mapping Value"""
    value: int
    ratelimit: bool

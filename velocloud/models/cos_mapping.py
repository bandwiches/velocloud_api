from dataclasses import dataclass
from velocloud.models.cos_mapping_value import CosMappingValue


@dataclass
class CosMapping:
    """CoS Mapping"""
    high: CosMappingValue = None
    normal: CosMappingValue = None
    low: CosMappingValue = None

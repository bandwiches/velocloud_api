from dataclasses import dataclass, field
from typing import List
from velocloud.models.configuration_module_segment_metadata import ConfigurationModuleSegmentMetadata
from velocloud.models.qos_business_rules import QosBusinessRules
from velocloud.models.cos_mapping import CosMapping


@dataclass
class CosMappingData:
    """CoS Mapping Data
    This is a custom class.
    """
    lsInputType: str = None
    bulk: CosMapping = None
    realtime: CosMapping = None
    transactional: CosMapping = None


@dataclass
class WebProxy:
    """QoS Web Proxy
    This is a custom class.
    """
    providers: List(dict) = None


@dataclass
class QosSegments:
    """QoS Segments"""
    rules: List(QosBusinessRules)
    webProxy: WebProxy
    segment: ConfigurationModuleSegmentMetadata
    defaults: List(QosBusinessRules) = field(default_factory=list)
    cosMapping: CosMappingData = None

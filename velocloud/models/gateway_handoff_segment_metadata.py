from dataclasses import dataclass
from velocloud.models.enums import configurationModuleSegmentType


@dataclass
class GatewayHandoffSegmentMetadata:
    """Gateway Handoff Segment Metadata"""
    name: str = None
    segmentId: int = None
    segmentLogicalId: str = None
    type: configurationModuleSegmentType = None

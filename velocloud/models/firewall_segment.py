from dataclasses import dataclass
from typing import List
from velocloud.models.firewall_outbound_rule import FirewallOutboundRule
from velocloud.models.configuration_module_segment_metadata import ConfigurationModuleSegmentMetadata


@dataclass
class FirewallSegment:
    """Firewall Segment"""
    firewall_logging_enabled: bool
    outbound: List(FirewallOutboundRule)
    segment: ConfigurationModuleSegmentMetadata
    stateful_firewall_enabled: bool = None

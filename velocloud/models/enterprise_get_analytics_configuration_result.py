from dataclasses import dataclass

from velocloud.models.enums import enterpriseAnalyticsCapability


@dataclass
class EnterpriseGetAnalyticsConfigurationResult:
    """ENterprise Get Analytics Configuration Result"""
    analyticsCapability: enterpriseAnalyticsCapability = None
    analyticsEdgeLimit: int = None

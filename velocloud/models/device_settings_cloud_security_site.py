from dataclasses import dataclass

from velocloud.models.cloud_security_service_site_data import CloudSecurityServiceSiteData


@dataclass
class DeviceSettingsCloudSecuritySite:
    """Device Settings Cloud Security Site"""
    data: CloudSecurityServiceSiteData = None
    logicalId: str = None

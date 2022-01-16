from dataclasses import dataclass
from velocloud.models.nvs_from_edge_site_data import NvsFromEdgeSiteData


@dataclass
class DeviceSettingsNvsFromEdgeSite:
    """Device Settings NVS From Edge Site"""
    data: NvsFromEdgeSiteData = None
    logicalId: str = None

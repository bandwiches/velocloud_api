from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import eventBaseCategory, eventBaseSeverity
from velocloud.models.vnf_image_download_event_detail import VnfImageDownloadEventDetail


@dataclass
class VnfImageDownloadEvent:
    """VNF Image Download Event"""
    id: int
    eventTime: datetime  # datetime
    event: str
    category: eventBaseCategory
    severity: eventBaseSeverity
    detail: VnfImageDownloadEventDetail
    message: str = None

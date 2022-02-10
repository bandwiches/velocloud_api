from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import tinyint


@dataclass
class EdgeLicense:
    """Edge License"""
    id: int = None
    created: datetime = None  # datetime
    licenseId: int = None
    sku: str = None
    name: str = None
    alias: str = None
    detail: str = None
    quota: str = None
    termMonths: int = None
    start: datetime = None  # datetime
    end: datetime = None  # datetime
    edition: str = None
    bandwidthTier: str = None
    active: tinyint = None
    modified: datetime = None  # datetime

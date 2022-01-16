from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import unitName, unitType
from velocloud.models.genericRefs import GenericRefs
from velocloud.models.wan_data import WanData


@dataclass
class Wan:
    """WAN"""
    name: unitName
    data: WanData
    created: datetime = None  # datetime
    effective: datetime = None  # datetime
    modified: datetime = None  # datetime
    id: int = None
    type: unitType = None
    description: str = None
    configurationId: int = None
    schemaVersion: str = None
    version: str = None
    metadata: dict = None
    refs: GenericRefs = None

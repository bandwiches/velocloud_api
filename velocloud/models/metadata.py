from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import unitName, unitType
from velocloud.models.metadata_data import MetadataData


@dataclass
class Metadata:
    """Metadata"""
    name: unitName
    data: MetadataData
    created: datetime = None  # datetime
    modified: datetime = None  # datetime
    effective: datetime = None  # datetime
    id: int = None
    type: unitType = None
    description: str = None
    configurationId: int = None
    schemaVersion: str = None
    version: str = None
    metadata: dict = None
    refs: dict = None

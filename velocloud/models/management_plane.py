from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import unitName, unitType
from velocloud.models.management_plane_data import ManagementPlaneData


@dataclass
class ManagementPlane:
    """Management Plane"""
    name: unitName
    data: ManagementPlaneData
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
    refs: dict = None

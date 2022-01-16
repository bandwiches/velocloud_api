from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import unitName, unitType
from velocloud.models.qos_data import QosData
from velocloud.models.qos_refs import QosRefs


@dataclass
class Qos:
    """QOS"""
    name: unitName
    data: QosData
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
    refs: QosRefs = None

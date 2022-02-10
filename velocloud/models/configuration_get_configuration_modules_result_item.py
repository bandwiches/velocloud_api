from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import unitName, unitType


@dataclass
class ConfigurationGetConfigurationModulesResultItem:
    """Configuration Get Configuration Modules Result Item"""
    id: int
    name: unitName
    type: unitType
    description: str
    configurationId: int
    data: dict
    refs: dict
    created: datetime = None  # datetime
    effective: datetime = None  # datetime
    modified: datetime = None  # datetime
    schemaVersion: str = None
    version: str = None
    metadata: dict = None

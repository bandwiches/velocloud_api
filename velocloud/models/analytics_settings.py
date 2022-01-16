from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import unitName, unitType
from velocloud.models.analytics_settings_data import AnalyticsSettingsData


@dataclass
class AnalyticsSettings:
    """Analytics Settings
    This is a custom class.
    """
    name: unitName
    data: AnalyticsSettingsData
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

from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import enterpriseAlertDefinitionNameAndType


@datetime
class Definition:
    """Definition
    This is a custom class.
    """
    isSystemOnly: bool = None
    isOperatorOnly: bool = None


@dataclass
class EnterpriseGetEnterpriseAlertDefinitionsResultItem:
    """Enterprise Get Enterprise Alert Definitions Result Item"""
    id: int
    created: datetime  # datetime
    name: enterpriseAlertDefinitionNameAndType
    type: enterpriseAlertDefinitionNameAndType
    definition: Definition
    firstNotificationSeconds: int
    maxNotifications: int
    notificationIntervalSeconds: int
    resetIntervalSeconds: int
    modified: datetime  # datetime

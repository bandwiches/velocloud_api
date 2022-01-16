from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import enterpriseAlertDefinitionNameAndType


@dataclass
class Definition:
    """Enterprise Alert Definition Definition
    This is a custom class.
    """
    isSystemOnly: bool = None
    isOperatorOnly: bool = None


@dataclass
class EnterpriseAlertDefinition:
    """Enterprise Alert Definition"""
    id: int = None
    created: datetime = None  # datetime
    name: enterpriseAlertDefinitionNameAndType = None
    type: enterpriseAlertDefinitionNameAndType = None
    definition: Definition = None
    firstNotificationSeconds: int = None
    maxNotifications: int = None
    notificationIntervalSeconds: int = None
    resetIntervalSeconds: int = None
    modified: datetime = None  # datetime

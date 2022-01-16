from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import enterpriseAlertDefinitionNameAndType


@dataclass
class Definition:
    """Enterprise Alert Configuration Definition
    This is a custom class.
    """
    isSystemOnly: bool = None
    isOperatorOnly: bool = None


@dataclass
class EnterpriseAlertConfiguration:
    """Enterprise Alert Configuration"""
    id: int = None
    created: datetime = None  # datetime
    alertDefinitionId: int = None
    enterpriseId: int = None
    enabled: bool = None
    name: enterpriseAlertDefinitionNameAndType = None
    description: str = None
    type: enterpriseAlertDefinitionNameAndType = None
    definition: Definition = None
    firstNotificationSeconds: int = None
    maxNotifications: int = None
    notificationIntervalSeconds: int = None
    resetIntervalSeconds: int = None
    modified: datetime = None  # datetime

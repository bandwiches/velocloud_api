from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import enterpriseAlertDefinitionNameAndType


@dataclass
class Definition:
    """Definition
    This is a custom class.
    """
    isSystemOnly: bool = None
    isOperatorOnly: bool = None


@dataclass
class EnterpriseGetEnterpriseAlertConfigurationsResultItem:
    """Enterprise Get Enterprise Alert Configurations Result Item"""
    id: int
    created: datetime  # datetime
    alertDefinitionId: int
    enterpriseId: int
    enabled: bool
    name: enterpriseAlertDefinitionNameAndType
    description: str
    type: enterpriseAlertDefinitionNameAndType
    definition: Definition
    firstNotificationSeconds: int
    maxNotifications: int
    notificationIntervalSeconds: int
    resetIntervalSeconds: int
    modified: datetime  # datetime

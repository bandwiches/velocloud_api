from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import enterpriseAlertDefinitionNameAndType, enterpriseAlertTriggerState


@dataclass
class EnterpriseAlertTrigger:
    """Enterprise Alert Trigger"""
    id: int = None
    created: datetime = None  # datetime
    triggerTime: datetime = None  # datetime
    enterpriseAlertConfigurationId: int = None
    enterpriseId: int = None
    edgeId: int = None
    edgeName: str = None
    linkId: int = None
    linkName: str = None
    enterpriseObjectId: int = None
    enterpriseObjectName: str = None
    name: enterpriseAlertDefinitionNameAndType = None
    type: enterpriseAlertDefinitionNameAndType = None
    state: enterpriseAlertTriggerState = None
    stateSetTime: datetime = None  # datetime
    lastContact: datetime = None  # datetime
    firstNotificationSeconds: int = None
    maxNotifications: int = None
    notificationIntervalSeconds: int = None
    resetIntervalSeconds: int = None
    comment: str = None
    nextNotificationTime: datetime = None  # datetime
    remainingNotifications: int = None
    timezone: str = None
    locale: str = None
    modified: datetime = None  # datetime

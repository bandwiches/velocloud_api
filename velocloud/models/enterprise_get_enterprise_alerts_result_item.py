from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from velocloud.models.enums import enterpriseAlertDefinitionNameAndType, enterpriseAlertTriggerState
from velocloud.models.enterprise_alert_notification import EnterpriseAlertNotification


@dataclass
class EnterpriseGetEnterpriseAlertsResultItem:
    """Enterprise Get Enterprise Alerts Result Item"""
    id: int
    created: datetime  # datetime
    triggerTime: datetime  # datetime
    enterpriseAlertConfigurationId: int
    enterpriseId: int
    edgeId: int
    edgeName: str
    linkId: int
    linkName: str
    enterpriseObjectId: int
    enterpriseObjectName: str
    name: enterpriseAlertDefinitionNameAndType
    type: enterpriseAlertDefinitionNameAndType
    state: enterpriseAlertTriggerState
    stateSetTime: datetime  # datetime
    lastContact: datetime  # datetime
    firstNotificationSeconds: int
    maxNotifications: int
    notificationIntervalSeconds: int
    resetIntervalSeconds: int
    comment: str
    nextNotificationTime: datetime  # datetime
    remainingNotifications: int
    timezone: str
    locale: str
    modified: datetime  # datetime
    notifications: List(EnterpriseAlertNotification) = field(default_factory=list)

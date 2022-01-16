from dataclasses import dataclass, field
from typing import List
from velocloud.models.enterprise_alert_notification_user_data import EnterpriseAlertNotificationUserData


@dataclass
class EnterpriseAlertNotification:
    """Enterprise Alert Notification"""
    id: int = None
    enterpriseAlertTriggerId: int = None
    enterpriseId: int = None
    created: str = None
    enterpriseUserList: List[EnterpriseAlertNotificationUserData] = field(default_factory=list)
    smsEnabled: int = None
    smsList: str = None
    smsText: str = None
    emailenabled: int = None
    emailList: str = None
    emailText: str = None
    mobileenabled: int = None
    mobileList: str = None
    mobileText: str = None
    snmpEnabled: int = None
    snmpList: str = None
    modified: str = None

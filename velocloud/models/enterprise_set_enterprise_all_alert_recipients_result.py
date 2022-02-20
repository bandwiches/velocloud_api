from dataclasses import dataclass, field
from typing import List
from velocloud.models.enterprise_alert_notification_user_data import EnterpriseAlertNotificationUserData


@dataclass
class EnterpriseSetEnterpriseAllAlertRecipientsResult:
    """Enterprise Set Enterprise All Alert Recipients Result"""
    emailEnabled: bool
    emailList: List(str)
    enterpriseUsers: List(EnterpriseAlertNotificationUserData)
    mobileEnabled: bool
    mobileList: List(str)
    smsEnabled: bool
    smsList: List(str)
    snmpEnabled: bool = None
    snmpList: List(str) = field(default_factory=list)
    webhookEnabled: bool = None
    webhookList: dict = None

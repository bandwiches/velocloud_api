from dataclasses import dataclass
from typing import List
from velocloud.models.enterprise_alert_notification_user_data import EnterpriseAlertNotificationUserData


@dataclass
class EnterpriseGetEnterpriseAllAlertRecipientsResult:
    """Enterprise Get Enterprise All Alert Recipients Result"""
    emailEnabled: bool
    emailList: List(str)
    enterpriseUsers: List(EnterpriseAlertNotificationUserData)
    mobileEnabled: bool
    mobileList: List(str)
    smsEnabled: bool
    smsList: List(str)
    snmpEnabled: bool
    snmpList: List(str)
    webhookEnabled: bool
    webhookList: dict

from dataclasses import dataclass


@dataclass
class EnterpriseAlertNotificationUserData:
    """Enterprise Alert Notification User Data"""
    email: str
    emailEnabled: int
    enabled: int
    enterpriseUserId: int
    mobileEnabled: int
    mobilePhone: str
    smsEnabled: int
    username: str

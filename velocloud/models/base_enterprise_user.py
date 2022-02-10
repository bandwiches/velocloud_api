from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import tinyint


@dataclass
class BaseEnterpriseUser:
    """Base Enterprise User"""
    id: int = None
    created: datetime = None  # datetime
    userType: str = None
    username: str = None
    domain: str = None
    password: str = None
    firstName: str = None
    lastName: str = None
    officePhone: str = None
    mobilePhone: str = None
    isNative: tinyint = None
    isActive: tinyint = None
    isLocked: tinyint = None
    disableSecondFactor: tinyint = None
    email: str = None
    lastLogin: datetime = None  # datetime
    modified: datetime = None  # datetime
    salt: str = None
    passwordModified: datetime = None  # datetime

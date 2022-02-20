from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import tinyint


@dataclass
class EnterpriseUserWithRoleInfo:
    """Enterprise User With Role Info"""
    id: int
    created: datetime
    userType: str
    username: str
    domain: str
    password: str
    firstName: str
    lastName: str
    officePhone: str
    mobilePhone: str
    isNative: tinyint
    isActive: tinyint
    isLocked: tinyint
    disableSecondFactor: tinyint
    email: str
    lastLogin: datetime
    modified: datetime
    salt: str
    passwordModified: datetime
    roleId: int
    roleName: str
    isSuper: tinyint

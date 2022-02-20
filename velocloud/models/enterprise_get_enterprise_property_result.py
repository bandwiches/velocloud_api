from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import enterprisePropertyDataType


@dataclass
class EnterpriseGetEnterprisePropertyResult:
    """Enterprise Get Enterprise Property Result"""
    id: int
    enterpriseId: int
    created: datetime
    name: str
    values: str
    isPassword: bool
    datatype: enterprisePropertyDataType
    description: str
    modified: datetime

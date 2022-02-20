from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import enterprisePropertyDataType


@dataclass
class EnterpriseProperty:
    """Enterprise Property"""
    id: int = None
    enterpriseId: int = None
    created: datetime = None
    name: str = None
    value: str = None
    isPassword: bool = None
    dataType: enterprisePropertyDataType = None
    description: str = None
    modified: datetime = None

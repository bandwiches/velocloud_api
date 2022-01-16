from dataclasses import dataclass
from velocloud.models.authentication_service_data import AuthenticationServiceData


@dataclass
class AuthenticationService:
    """Authentication Service"""
    type: str
    id: int = None
    enterpriseObjectId: int = None
    configurationId: int = None
    moduleId: int = None
    ref: str = None
    data: AuthenticationServiceData = None
    version: str = None
    object: str = None
    name: str = None
    logicalId: str = None

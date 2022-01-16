from dataclasses import dataclass


@dataclass
class EnterpriseService:
    """Enterprise Service"""
    id: int = None
    enterpriseObjectId: int = None
    configurationId: int = None
    moduleId: int = None
    ref: str = None
    data: dict = None
    version: str = None
    object: str = None
    name: str = None
    type: str = None
    logicalId: str = None

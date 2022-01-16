from dataclasses import dataclass


@dataclass
class Ref:
    """Ref"""
    configurationId: int
    moduleId: int
    logicalId: str
    enterpriseObjectId: int
    segmentLogicalId: str
    segmentObjectId: int
    id: int = None
    ref: str = None

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


""" ENUMS """


class DRClientType(Enum):
    EDGE = "EDGE"
    GATEWAY = "GATEWAY"


""" DATACLASSES """


@dataclass
class DRClientContact:
    activeAddress: str
    activeLastResponseTime: datetime
    clientLogicalId: str
    clientType: DRClientType
    id: int
    modified: datetime
    standbyLastResponseTime: datetime

    def __repr__(self):
        return str(type(self))

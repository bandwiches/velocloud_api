from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import tinyint
from velocloud.models.netflow_filter_data import NetflowFilterData


@dataclass
class NetflowFilter:
    """Netflow Filter"""
    id: int
    created: datetime  # datetime
    operatorId: int
    networkId: int
    enterpriseId: int
    edgeId: int
    gatewayId: int
    parentGroupId: int
    description: str
    object: str
    name: str
    type: str
    logicalId: str
    alertsEnabled: tinyint
    operatorAlertsEnabled: tinyint
    status: str
    statusModified: datetime  # datetime
    previousData: dict
    previousCreated: datetime  # datetime
    draftData: str
    draftCreated: datetime  # datetime
    draftComment: str
    data: NetflowFilterData
    lastContact: datetime  # datetime
    version: str
    modified: datetime  # datetime

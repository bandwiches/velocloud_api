from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import tinyint
from velocloud.models.netflow_collector_data import NetflowCollectorData


@dataclass
class NetflowCollector:
    """Netflow Collector"""
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
    draftCreated: datetime
    draftComment: str
    data: NetflowCollectorData
    lastContact: datetime  # datetime
    version: str
    modified: datetime  # datetime

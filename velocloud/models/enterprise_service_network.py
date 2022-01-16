from dataclasses import dataclass
from velocloud.models.enterprise_service_network_data import EnterpriseServiceNetworkData


@dataclass
class EnterpriseServiceNetwork:
    """Enterprise Service Netowrk"""
    id: int = None
    enterpriseObjectId: int = None
    configurationId: int = None
    moduleId: int = None
    ref: str = None
    data: EnterpriseServiceNetworkData = None
    version: str = None
    object: str = None
    name: str = None
    type: str = None
    logicalId: str = None

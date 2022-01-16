from dataclasses import dataclass
from velocloud.models.dns_data import DnsData


@dataclass
class Dns:
    """DNS"""
    type: str
    id: int = None
    enterpriseObjectId: int = None
    configurationId: int = None
    moduleId: int = None
    ref: str = None
    data: DnsData = None
    version: str = None
    object: str = None
    name: str = None
    logicalId: str = None

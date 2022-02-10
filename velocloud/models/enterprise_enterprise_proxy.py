from dataclasses import dataclass
from datetime import datetime

from velocloud.models.enums import enterpriseProxyType


@dataclass
class EnterpriseEnterpriseProxy:
    """Enterprise Enterprise Proxy"""
    id: int
    created: datetime  # datetime
    networkId: int
    proxyType: enterpriseProxyType
    operateGateways: bool
    logicalId: str
    name: str
    domain: str
    prefix: str
    description: str
    contactName: str
    contactPhone: str
    contactMobile: str
    contactEmail: str
    streetAddress: str
    streetAddress2: str
    city: str
    state: str
    postalCode: str
    country: str
    lat: float
    lon: float
    modified: datetime  # datetime

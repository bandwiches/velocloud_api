from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import enterpriseProxyType


@dataclass
class EnterpriseProxy:
    """Enterprise Proxy"""
    id: int = None
    created: datetime = None
    networkId: int = None
    proxyType: enterpriseProxyType = None
    operateGateways: bool = None
    logicalId: str = None
    name: str = None
    domain: str = None
    prefix: str = None
    description: str = None
    contactname: str = None
    contactPhone: str = None
    contactMobile: str = None
    contactEmail: str = None
    streetAddress: str = None
    streetAddress2: str = None
    city: str = None
    state: str = None
    postalCode: str = None
    country: str = None
    lat: float = None
    lon: float = None
    modified: datetime = None  # datetime

    def __repr__(self):
        return str(type(self))

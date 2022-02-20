from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from velocloud.models.enterprise_object import EnterpriseObject
from velocloud.models.enums import tinyint, endpointPkiMode as ePM


@dataclass
class EnterpriseProxyGetEnterpriseProxyEnterpriseResultItem:
    """Enterprise Proxy Get Enterprise Proxy Enterprise Result Item"""
    id: int = None
    created: datetime = None
    networkId: int = None
    gatewayPoolId: tinyint = None
    operatorAlertsEnabled: tinyint = None
    endpointPkiMode: ePM = None
    name: str = None
    domain: str = None
    prefix: str = None
    logicalId: str = None
    accountNumber: str = None
    description: str = None
    contactName: str = None
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
    timezone: str = None
    locale: str = None
    modified: datetime = None
    edgeCount: int = None
    edges: List(EnterpriseObject) = field(default_factory=list)

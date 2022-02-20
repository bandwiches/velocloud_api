from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import endpointPkiMode as ePM, tinyint
from velocloud.models.enterprise_enterprise_proxy import EnterpriseEnterpriseProxy


@dataclass
class EnterpriseGetEnterpriseResult:
    """Enterprise Get Enterprise Result"""
    id: int
    created: datetime  # datetime
    networkId: int
    gatewayPoolId: int
    alertsEnabled: tinyint
    operatorAlertsEnabled: tinyint
    endpointPkiMode: ePM
    name: str
    domain: str
    prefix: str
    logicalId: str
    accountNumber: str
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
    timezone: str
    locale: str
    modified: datetime  # datetime
    enterpriseProxy: EnterpriseEnterpriseProxy = None

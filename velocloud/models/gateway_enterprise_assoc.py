from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import enterpriseGatewayType, tinyint, endpointPkiMode as ePM


@dataclass
class GatewayEnterpriseAssoc:
    """Gateway Enterprise Assoc"""
    id: int = None
    created: datetime = None
    networkId: int = None
    gatewayPoolId: int = None
    alertsEnabled: tinyint = None
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
    enterpriseId: int = None
    enterpriseObjectId: int = None
    edgeId: int = None
    gatewayType: enterpriseGatewayType = None
    pinned: int = None
    enterpriseObjectName: str = None
    enterpriseObjectType: str = None
    edgeName: str = None
    edgeLogicalId: str = None

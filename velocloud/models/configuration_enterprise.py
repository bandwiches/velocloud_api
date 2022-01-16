from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import tinyint, endpointPkiMode as ePkiMode


@dataclass
class ConfigurationEnterprise:
    """Configuration Enterprise"""
    id: int = None
    created: datetime = None  # datetime
    networkId: str = None
    gatewayPoolId: str = None
    alertsEnabled: tinyint = None
    operatorAlertsEnabled: tinyint = None
    endpointPkiMode: ePkiMode = None
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
    modified: datetime = None  # datetime
    configurationAssociationId: int = None

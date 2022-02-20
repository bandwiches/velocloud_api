from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import tinyint
from velocloud.models.auth_object import AuthObject


@dataclass
class EnterpriseObject:
    """Enterprise Object"""
    id: int = None
    created: datetime = None
    name: str = None
    logicalId: str = None
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
    shippingSameAsLocation: tinyint = None
    shippingContactName: str = None
    shippingAddress: str = None
    shippingAddress2: str = None
    shippingCity: str = None
    shippingState: str = None
    shippingCountry: str = None
    shippingPostalCode: str = None
    modified: datetime = None
    gatewayPoolId: int = None
    networkId: int = None
    returnData: bool = None
    user: AuthObject = None

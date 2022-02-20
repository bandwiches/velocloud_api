from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from velocloud.models.enums import tinyint
from velocloud.models.auth_object import AuthObject


@dataclass
class License:
    """License
    This is a custom class.
    """
    ids: List(int) = field(default_factory=list)


@dataclass
class EnterpriseProxyInsertEnterpriseProxyEnterprise:
    """Enterprise Proxy Insert Enterprise Proxy Enterprise"""
    name: str
    configurationId: int
    id: int = None
    created: datetime = None
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
    shippingPostalCode: str = None
    modified: datetime = None
    gatewayPoolId: int = None
    networkId: int = None
    returnData: bool = None
    user: AuthObject = None
    enableEnterpriseDelegationToOperator: bool = None
    enableEnterpriseDelegationToProxy: bool = None
    enableEnterpriseUserManagementDelegationToOperator: bool = None
    delegateEdgeImageManagementToEnterprise: bool = None
    enableExportRestriction: bool = None
    assignedOperatorProfileConfigurationIds: List(int) = field(default_factory=list)
    licenses: List(License) = field(default_factory=list)
    enterpriseProxyId: int = None

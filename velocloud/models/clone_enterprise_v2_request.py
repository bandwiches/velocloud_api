from dataclasses import dataclass, field
from typing import List
from datetime import datetime
from velocloud.models.enums import tinyint


@dataclass
class License:
    """License
    This is a custom class.
    """
    ids: List(int) = field(default_factory=list)


@dataclass
class User:
    """User
    This is a custom class.
    """
    password: str
    username: str
    email: str = None
    password2: str = None
    firstName: str = None
    lastName: str = None
    officePhone: str = None
    officePhone: str = None


@dataclass
class CloneEnterpriseV2Request:
    """Clone Enterprise v2 Request"""
    id: int
    name: str
    user: User
    configurationId: int
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
    modified: datetime = None
    enableEnterpriseDelegationToOperator: bool = None
    enableEnterpriseDelegationToProxy: bool = None
    enableEnterpriseUserManagementDelegationToOperator: bool = None
    delegateEdgeImageManagementToEnterprise: bool = None
    enableExportRestriction: bool = None
    assignedOperatorProfileConfigurationIds: List(int) = field(default_factory=list)
    gatewayPoolId: int = None
    networkId: int = None
    accountNumber: str = None
    licenses: List(License) = field(default_factory=list)
    _with: List(str) = field(default_factory=list)

    @property
    def withs(self):
        """with Getter"""
        return self._with

    @withs.setter
    def withs(self, value: list):
        """with Setter"""
        self._with = value

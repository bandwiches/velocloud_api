import aiohttp
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import logging
from typing import List
from velocloud.models.session import VCO
from velocloud.models.configuration import ConfigurationType, ConfigurationModule
from velocloud.orchestrator import error_handlers


LOGGER = logging.getLogger('velocloud.models.enterprise')
BASE_ENDPOINT = '/portal/rest/enterprise'


"""Enums"""


class ProxyType(Enum):
    PARTNER = "PARTNER"
    MSP = "MSP"


"""Dataclasses"""


@dataclass
class AuthObject:
    username: str
    password: str
    email: str = None
    password2: str = None

    def __repr__(self):
        return str(type(self))

    @classmethod
    def from_dict(cls, profile: dict):
        """Factory Method"""
        INST = cls()
        INST.username = profile.get('username')
        INST.password = profile.get('password')
        INST.email = profile.get('email')
        INST.password2 = profile.get('password2')

        return INST


@dataclass
class EnterpriseAlertNotificationUserData:
    email: str
    emailEnabled: int
    enabled: int
    enterpriseUserId: int
    mobileEnabled: int
    mobilePhone: str
    smsEnabled: int
    username: str


@dataclass
class EnterpriseAlertNotification:
    id: int = None
    enterpriseAlertTriggerId: int = None
    enterpriseId: int = None
    created: str = None
    enterpriseUserList: List[EnterpriseAlertNotificationUserData] = field(default_factory=list)
    smsEnabled: int = None
    smsList: str = None
    smsText: str = None
    emailenabled: int = None
    emailList: str = None
    emailText: str = None
    mobileenabled: int = None
    mobileList: str = None
    mobileText: str = None
    snmpEnabled: int = None
    snmpList: str = None
    modified: str = None


@dataclass
class EnterpriseConfigurationItem:
    created: datetime = None
    description: str = None
    effective: datetime = None
    _id: int = None
    modified: datetime = None
    name: str = None
    version: str = None
    configurationType: ConfigurationType = None
    edgeCount: int = None
    logicalId: str = None
    modules: List[ConfigurationModule] = field(default_factory=list)
    schemaVersion: str = None
    isStaging: int = None
    edges: List[dict] = field(default_factory=list)

    def __repr__(self) -> str:
        return str(type(self))

    @property
    def configuration_id(self) -> int:
        return self._id

    @classmethod
    def from_dict(cls, profile: dict):
        """Factory Method"""
        INST = cls()
        INST.created = datetime.strptime(profile["created"], "%Y-%m-%dT%H:%M:%S.%fZ")
        INST.description = profile.get('description')
        INST.effective = datetime.strptime(profile["effective"], "%Y-%m-%dT%H:%M:%S.%fZ")
        INST._id = profile.get('id')
        INST.modified = datetime.strptime(profile["modified"], "%Y-%m-%dT%H:%M:%S.%fZ")
        INST.name = profile.get('name')
        INST.version = profile.get('version')
        INST.configurationType = ConfigurationType(profile.get('configurationType'))
        INST.edgeCount = profile.get('edgeCount')
        INST.logicalId = profile.get('logicalId')
        if 'modules' in profile.keys():
            for m in profile.get('modules'):
                INST.modules.append(ConfigurationModule.from_dict(m))
        INST.schemaVersion = profile.get('schemaVersion')
        INST.isStaging = profile.get('isStaging')
        if 'edges' in profile.keys():
            for e in profile.get('edges'):
                INST.edges.append(e)

        return INST


@dataclass
class EnterpriseProxy:
    _id: int
    created: datetime
    networkId: int
    proxyType: ProxyType
    operateGateways: bool
    logicalId: str
    name: str
    domain: str
    prefix: str
    description: str
    contactname: str
    contactPhone: str
    contactMobile: str
    contactEmail: str
    streetAddress: str
    streetAddress2: str
    city: str
    state: str
    postalCode: str
    lat: float
    lon: float
    modified: datetime

    def __repr__(self):
        return str(type(self))

    @property
    def enterprise_proxy_id(self):
        return self._id


@dataclass
class EnterpriseBase:
    _id: int
    created: datetime
    operatorId: int
    networkId: int
    entepriseId: int
    edgeid: int
    gatewayId: int
    parentGroupId: int
    description: str
    object: str
    name: str
    type: str
    logicalId: str
    alertsEnabled: int
    operatorAlertsEnabled: int
    status: str
    statusModified: datetime
    previousData: dict
    previousCreated: datetime
    draftData: str
    draftCreated: datetime
    draftComment: str
    data: dict
    lastContact: datetime
    version: str
    modified: str

    def __repr__(self):
        return str(type(self))

    @property
    def enterprise_id(self):
        return self._id


@dataclass
class Enterprise(EnterpriseBase):
    _id: int
    created: datetime  # Datetime
    name: str
    logicalId: str
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
    shippingSameAsLocation: int
    shippingContactName: str
    shippingAddress: str
    shippingAddress2: str
    shippingCity: str
    shippingState: str
    shippingCountry: str
    shippingPostalCode: str
    modified: datetime
    gatewayPoolId: int
    networkId: int
    returnData: bool
    user: AuthObject = None

    def __repr__(self):
        return str(type(self))

    @property
    def enterprise_id(self):
        return self._id

    @classmethod
    def from_dict(cls, profile: dict):
        """Factory Method"""
        INST = cls()
        INST._id = profile.get('id')
        try:
            INST.created = datetime.strptime(profile.get('created'), "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        INST.name = profile.get('name')
        INST.logicalId = profile.get('logicalId')
        INST.contactName = profile.get('contactName')
        INST.contactPhone = profile.get('contactPhone')
        INST.contactMobile = profile.get('contactMobile')
        INST.contactEmail = profile.get('contactEmail')
        INST.streetAddress = profile.get('streetAddress')
        INST.streetAddress2 = profile.get('streetAddress2')
        INST.city = profile.get('city')
        INST.state = profile.get('state')
        INST.postalCode = profile.get('postalCode')
        INST.country = profile.get('country')
        INST.lat = profile.get('lat')
        INST.lon = profile.get('lon')
        INST.timezone = profile.get('timezone')
        INST.locale = profile.get('locale')
        INST.shippingSameAsLocation = profile.get('shippingSameAsLocation')
        INST.shippingContactName = profile.get('shippingContactName')
        INST.shippingAddress = profile.get('shippingAddress')
        INST.shippingAddress2 = profile.get('shippingAddress2')
        INST.shippingCity = profile.get('shippingCity')
        INST.shippingState = profile.get('shippingState')
        INST.shippingCountry = profile.get('shippingCountry')
        INST.shippingPostalCode = profile.get('shippingPostalCode')
        try:
            INST.modified = datetime.strptime(profile.get('modified'), "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        INST.gatewayPoolId = profile.get('gatewayPoolId')
        INST.networkId = profile.get('networkId')
        INST.returnData = profile.get('returnData')
        INST.user = AuthObject.from_dict(profile.get('user'))

        return INST

    @staticmethod
    async def getEnterprise(session: VCO, enterprise_id: int = None, extras: list = None):
        """Get Enterprise

        Profiles, etc...

        Args:
            session (VCO): Velocloud Session Object
            (Optional) extras (list): A list of extra fields to retrieve (enterpriseProxy)

        Returns:
            Enterprise: An Enterprise Object
        """
        ENDPOINT = f'{BASE_ENDPOINT}/getEnterprise'
        URL = f'{session.API_URL}{ENDPOINT}'
        BODY = {}

        if enterprise_id is not None:
            BODY["enterpriseId"] = enterprise_id
        if extras is not None:
            BODY["with"] = extras

        LOGGER.info(f'[{enterprise_id}] Requesting Enterprise...')

        async with aiohttp.request('POST', URL, headers=session.get_headers(), json=BODY) as api_request:
            if api_request.status != 200:
                status = api_request.status
                error_data = await api_request.json()
                formatted_error = await error_handlers.format_error(status, error_data)
                raise Exception(f'{formatted_error.code}: {formatted_error.message}')

            data = await api_request.json()
            LOGGER.debug(data)

            LOGGER.info(f'{data["name"]} [{data["id"]}]: Enterprise retrieved successfully.')

        return Enterprise.from_dict(data)

    async def get_enterprise_configurations(self, session: VCO, configType: ConfigurationType = None, extras: list = None) -> list:
        """Get Enterprise Configurations

        Profiles, etc...

        Args:
            session (VCO): Velocloud Session Object
            (Optional) configType (ConfigurationType): Enum
            (Optional) extras (list): A list of extra fields to retrieve (edges, modules, edgeCount, refs, deviceSettings)
                - Needs love

        Returns:
            None
        """
        ENDPOINT = f'{BASE_ENDPOINT}/getEnterpriseConfigurations'
        URL = f'{session.API_URL}{ENDPOINT}'
        BODY = {"enterpriseId": int(self.enterprise_id)}
        RESULTS = []

        if ConfigurationType is not None:
            BODY["configurationType"] = str(configType)
        if extras is not None:
            BODY["with"] = extras

        LOGGER.info(f'{self.name} [{self.enterprise_id}]: Requesting enterprise configurations...')

        async with aiohttp.request('POST', URL, headers=session.get_headers(), json=BODY) as api_request:
            if api_request.status != 200:
                status = api_request.status
                error_data = await api_request.json()
                formatted_error = await error_handlers.format_error(status, error_data)
                raise Exception(f'{self.name} [{self.enterprise_id}]: {formatted_error.code}: {formatted_error.message}')

            data = await api_request.json()
            # Data is list
            LOGGER.debug(data)

        LOGGER.info(f'{self.name} [{self.edge_id}]: Enterprise configurations received successfully.')

        for c in data:
            RESULTS.append(EnterpriseConfigurationItem.from_dict(c))

        return RESULTS

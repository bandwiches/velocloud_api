import aiohttp
from dataclasses import dataclass, field
from datetime import datetime
import logging
from typing import List
from velocloud.models.session import VCO
from velocloud.orchestrator import error_handlers
from velocloud.models.enums import configurationModuleType, endpointPkiMode, tinyint


LOGGER = logging.getLogger('velocloud.models.enterprise')
BASE_ENDPOINT = '/portal/rest/enterprise'


"""Dataclasses"""


@dataclass
class EnterpriseConfigurationItem:
    """Enterprise Configuration Item
    This is a custom class.

    This was created originally as a quick response from the API.
    This needs to be reviewed and rewritten.
    """
    created: datetime = None
    description: str = None
    effective: datetime = None
    _id: int = None
    modified: datetime = None
    name: str = None
    version: str = None
    configurationType: configurationModuleType = None
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
        INST.configurationType = configurationModuleType(profile.get('configurationType'))
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
class Enterprise:
    """Enterprise"""
    id: int = None
    created: datetime = None  # datetime
    networkId: int = None
    gatewayPoolId: int = None
    alertsEnabled: tinyint = None
    operatorAlertsEnabled: tinyint = None
    endpointPkiMode: endpointPkiMode = None
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
        INST.networkId = profile.get('networkId')
        INST.gatewayPoolId = profile.get('gatewayPoolId')
        INST.alertsEnabled = tinyint(int(profile.get('alertsEnabled')))
        INST.operatorAlertsEnabled = tinyint(int(profile.get('operatorAlertsEnabled')))
        INST.endpointPkiMode = endpointPkiMode(profile.get('endpointPkiMode'))
        INST.name = profile.get('name')
        INST.domain = profile.get('domain')
        INST.prefix = profile.get('prefix')
        INST.logicalId = profile.get('logicalId')
        INST.accountNumber = profile.get('accountNumber')
        INST.description = profile.get('description')
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
        try:
            INST.modified = datetime.strptime(profile.get('modified'), "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
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

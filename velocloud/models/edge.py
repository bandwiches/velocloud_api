import aiohttp
from dataclasses import dataclass, field, asdict
from datetime import datetime
from enum import Enum
import logging
from typing import List
from velocloud.models.session import VCO
from velocloud.models.site import Site
from velocloud.models.enterprise import Enterprise
from velocloud.models.link import Link
from velocloud.models.configuration import ConfigurationModule, ConfigurationType, ModelConfiguration
from velocloud import orchestrator


LOGGER = logging.getLogger('velocloud.models.edge')
BASE_ENDPOINT = "/portal/rest/edge"


"""
    Enums
"""


class ActivationState(Enum):
    """Edge Activation State (v4.2.1)"""
    UNASSIGNED = 'UNASSIGNED'
    PENDING = 'PENDING'
    ACTIVATED = 'ACTIVATED'
    REACTIVATION_PENDING = 'REACTIVATION_PENDING'


class AnalyticsMode(Enum):
    """Analytics Mode (v4.2.1)"""
    SDWAN_ONLY = 'SDWAN_ONLY'
    SDWAN_ANALYTICS = 'SDWAN_ANALYTICS'
    ANALYTICS_ONLY = 'ANALYTICS_ONLY'


class EdgeClientVisibilityMode(Enum):
    MAC = "MAC"
    IP = "IP"


class EdgeState(Enum):
    """Edge State (v4.2.1)"""
    NEVER_ACTIVATED = "NEVER_ACTIVATED"
    DEGRADED = "DEGRADED"
    OFFLINE = "OFFLINE"
    DISABLED = "DISABLED"
    EXPIRED = "EXPIRED"
    CONNECTED = "CONNECTED"


class EndpointPkiMode(Enum):
    """Endpoint PKI Mode (v4.2.1)"""
    CERTIFICATE_DISABLED = "CERTIFICATE_DISABLED"
    CERTIFICATE_OPTIONAL = "CERTIFICATE_OPTIONAL"
    CERTIFICATE_REQUIRED = "CERTIFICATE_REQUIRED"


class HaState(Enum):
    """HA State (v4.2.1)"""
    UNCONFIGURED = "UNCONFIGURED"
    PENDING_INIT = "PENDING_INIT"
    PENDING_CONFIRMATION = "PENDING_CONFIRMATION"
    PENDING_CONFIRMED = "PENDING_CONFIRMED"
    PENDING_DISSOCIATION = "PENDING_DISSOCIATION"
    READY = "READY"
    FAILED = "FAILED"


class ModelNumber(Enum):
    """Edge Model Number (v4.2.1)"""
    edge500 = 'edge500'
    edge5x0 = 'edge5x0'
    edge510 = 'edge510'
    edge510lte = 'edge510lte'
    edge6x0 = 'edge6x0'
    edge610lte = 'edge610lte'
    edge840 = 'edge840'
    edge1000 = 'edge1000'
    edge1000qat = 'edge1000qat'
    edge3x00 = 'edge3x00'
    edge3x10 = 'edge3x10'
    virtual = 'virtual'


class PeerType(Enum):
    BRANCH = "BRANCH"
    HUB = "HUB"
    GATEWAY = "GATEWAY"


class ServiceState(Enum):
    """Service State (v4.2.1)"""
    IN_SERVICE = "IN_SERVICE"
    OUT_OF_SERVICE = "OUT_OF_SERVICE"
    PENDING_SERVICE = "PENDING_SERVICE"


"""
    Query Results
"""


@dataclass
class EdgeDeleteEdgeResultItem:
    rows: int
    id: int = None
    error: str = None


@dataclass
class EdgeRequestReactivationResult:
    activationKey: str
    activationKeyExpires: datetime


@dataclass
class EdgeCancelReactivationResult:
    rows: int
    error: str = None


@dataclass
class EdgeClientVisibilityModeResult:
    edgeClientVisibilityMode: EdgeClientVisibilityMode


@dataclass
class EdgeConfigurationModulesResult:
    """This is not standard"""
    deviceSettings: dict
    firewall: dict
    qos: dict
    wan: dict
    controlPlane: dict
    managementPlane: dict
    imageUpdate: dict


@dataclass
class EdgeConfigurationStackResultItem:
    created: datetime
    description: str
    id: int
    modified: datetime
    modules: List[ConfigurationModule]
    name: str
    version: str
    configurationType: ConfigurationType = None
    edgeCount: int = None
    effective: datetime = None
    logicalId: str = None
    schemaVersion: str = None
    isStaging: int = None


@dataclass
class EdgeConfigurationStackResult:
    items: List[EdgeConfigurationStackResultItem]


@dataclass
class EdgeSdwanPeersResultItem:
    """This is not standard"""
    edgeLogicalId: str = None
    deviceLogicalid: str = None
    peerName: str = None
    description: str = None
    peerType: PeerType = None
    scoreAfterVoice: float = None
    scoreAfterVideo: float = None
    scoreAfterTrans: float = None
    pathStatusCount: dict = None
    pathQoe: float = None


@dataclass
class EdgeSdwanPeersResult:
    items: List[EdgeSdwanPeersResultItem]


"""
    Usable Objects
"""


@dataclass
class EdgeProvision:
    """Provision a New Edge (v4.2.1)

    Requires:
        configurationId (int): Enteprise Profile ID
        modelNumber (ModelNumber): Edge Model
    """
    configurationId: int
    modelNumber: ModelNumber
    enterpriseId: int = None
    name: str = None
    serialNumber: str = None
    description: str = None
    site: Site = None
    haEnabled: bool = False
    generatedCertificate: bool = False
    subjectCN: str = None
    subjectO: str = None
    subjectOU: str = None
    challengePassword: str = None
    privateKeyPassword: str = None
    edgeLicenseId: int = None
    customInfo: str = None
    analyticsMode: AnalyticsMode = None

    def __repr__(self):
        return str(type(self))

    @classmethod
    def from_dict(cls, profile: dict):
        return None

    async def provision(self, session: VCO) -> dict:
        """Provision

        Args:
            session (VCO): Velocloud Orchestrator session

        Returns:
            tuple: Edge Name, Edge ID, Activation Key
        """
        ENDPOINT = f'{BASE_ENDPOINT}/edgeProvision'
        URL = f'{session.API_URL}{ENDPOINT}'
        BODY = {
            "configuartionId": int(self.configurationId),
            "modelNumber": str(self.modelNumber)
        }
        # Optional
        if self.enterpriseId:
            BODY["enterpriseId"] = int(self.enterpriseId)
        if self.name:
            BODY["name"] = str(self.name)
        if self.serialNumber:
            BODY["serialNumber"] = str(self.serialNumber)
        if self.description:
            BODY["description"] = str(self.description)
        if self.site:
            BODY["site"] = asdict(self.site)
        if self.haEnabled:
            BODY["haEnabled"] = bool(self.haEnabled)
        if self.generatedCertificate:
            BODY["generatedCertificate"] = bool(self.generatedCertificate)
        if self.subjectCN:
            BODY["subjectCN"] = str(self.subjectCN)
        if self.subjectO:
            BODY["subjectO"] = str(self.subjectO)
        if self.subjectOU:
            BODY["subjectOU"] = str(self.subjectOU)
        if self.challengePassword:
            BODY["challengePassword"] = str(self.challengePassword)
        if self.privateKeyPassword:
            BODY["privateKeyPassword"] = str(self.privateKeyPassword)
        if self.edgeLicenseId:
            BODY["edgeLicenseId"] = int(self.edgeLicenseId)
        if self.customInfo:
            BODY["customInfo"] = str(self.customInfo)
        if self.analyticsMode:
            BODY["subjectCN"] = str(self.analyticsMode)

        LOGGER.info(f'Provisioning New Edge {str(self.modelNumber)}...')

        async with aiohttp.request('POST', URL, headers=session.get_headers(), json=BODY) as api_request:
            if api_request.status != 200:
                status = api_request.status
                error_data = await api_request.json()
                formatted_error = await orchestrator.error_handlers.format_error(status, error_data)
                LOGGER.error(f'{self.name} [{self.edge_id}]: {formatted_error}')
                raise Exception(f'{formatted_error.code}: {formatted_error.message}')

            data = await api_request.json()

        return data


@dataclass
class EdgeConfigurationStackModule:
    """Edge Configuration Module

    WARNING: Will be depracated next update

    Some settings are located within the module.  Velocloud API is stupid.

    Included in self.module:
        - data (dict)
        - type (ConfigurationLevelType)
        - name (ConfigurationModuleType)
        - schemaVersion (str)
        - verions (str)

    Extras: SOME modules return extra information
    """
    _id: int = None
    created: datetime = None  # Datetime
    name: str = None  # Profile Name
    description: str = None
    configurationId: int = None
    modules: List[ConfigurationModule] = field(default_factory=(list))
    effective: datetime = None  # datetime
    modified: datetime = None  # datetime
    metadata: dict = None
    # Extras
    # only deviceSettings modules contain refs
    refs: dict = None

    def __repr__(self):
        """Object Representation"""
        return str(type(self))

    @classmethod
    def from_dict(cls, profile: dict):
        """Edge Configuration Module Factory"""
        inst = cls()
        inst._id = profile.get('id')
        try:
            inst.created = datetime.strptime(profile["created"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        inst.name = profile.get('name')
        inst.description = profile.get('description')
        inst.configurationId = profile.get('configurationId')
        # Modules
        modules = profile.get('modules')
        for mod in modules:
            module_profile = {
                'name': mod.get('name'),
                'version': mod.get('version'),
                'schemaVersion': mod.get('schemaVersion'),
                'type': mod.get('type'),
                'data': mod.get('data')
            }
            inst.modules.append(ConfigurationModule.from_dict(module_profile))
        try:
            inst.effective = datetime.strptime(profile["effective"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            inst.modified = datetime.strptime(profile["modified"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        # Extras
        inst.refs = profile.get('refs')  # deviceSettings module only
        return inst


@dataclass
class EdgeConfigurationStack:
    """Edge Configuration Stack

    WARNING: Will be depracated next update

    Configuration profiles applied to the edge.
    """
    profiles: List[EdgeConfigurationStackModule] = field(default_factory=(list))

    def __repr__(self):
        """Object Representation"""
        return str(type(self))

    @classmethod
    def from_list(cls, profile: list):
        """Edge Configuration Stack Factory"""
        inst = cls()
        for p in profile:
            inst.profiles.append(EdgeConfigurationStackModule.from_dict(p))
        return inst


@dataclass
class Edge:
    """ Edge (v4.2.1)"""
    activationKey: str = None
    activationKeyExpires: datetime = None  # Datetime
    activationState: ActivationState = None
    activationTime: datetime = None  # Datetime
    alertsEnabled: int = None
    buildNumber: str = None
    created: datetime = None  # Datetime
    customInfo: str = None
    description: str = None
    deviceFamily: str = None
    deviceId: str = None
    dnsName: str = None
    edgeState: EdgeState = None
    edgeStateTime: datetime = None  # Datetime
    endpointPkiMode: EndpointPkiMode = None
    enterpriseId: int = None
    factorySoftwareVersion: str = None
    factoryBuildNumber: str = None
    haLastContact: datetime = None  # Datetime
    haPreviousState: HaState = None
    haSerialNumber: str = None
    haState: HaState = None
    id: int = None
    isLive: int = None
    lastContact: datetime = None  # Datetime
    logicalId: str = None
    modelNumber: str = None
    modified: datetime = None  # Datetime
    name: str = None
    operatorAlertsEnabled: int = None
    selfMacAddress: str = None
    serialNumber: str = None
    serviceState: ServiceState = None
    serviceUpSince: datetime = None  # Datetime
    siteId: int = None
    softwareUpdated: datetime = None  # Datetime
    softwareVersion: str = None
    systemUpSince: datetime = None  # Datetime
    # Extras
    configuration: ModelConfiguration = None
    enterprise: Enterprise = None
    links: List[Link] = field(default_factory=list)
    recentLinks: List[Link] = field(default_factory=list)
    site: Site = None

    def __repr__(self):
        return str(type(self))

    @classmethod
    def from_dict(cls, profile: dict):
        """Edge Factory"""
        # Datetimes
        activationKeyExpires = None
        activationTime = None
        created = None
        edgeStateTime = None
        haLastContact = None
        lastContact = None
        modified = None
        serviceUpSince = None
        softwareUpdated = None
        systemUpSince = None
        # Extras
        configuration = None
        enterprise = None
        links = []
        recentLinks = []
        site = None

        # Datetime's
        try:
            activationKeyExpires = datetime.strptime(profile["activationKeyExpires"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            activationTime = datetime.strptime(profile["activationTime"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            created = datetime.strptime(profile["created"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            edgeStateTime = datetime.strptime(profile["edgeStateTime"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            haLastContact = datetime.strptime(profile["haLastContact"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            lastContact = datetime.strptime(profile["lastContact"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            modified = datetime.strptime(profile["modified"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            serviceUpSince = datetime.strptime(profile["serviceUpSince"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            softwareUpdated = datetime.strptime(profile["softwareUpdated"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            systemUpSince = datetime.strptime(profile["systemUpSince"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass

        # Extras
        if 'configuration' in profile.keys():
            configuration = ModelConfiguration.from_dict(profile["configuration"])
        if 'enterprise' in profile.keys():
            enterprise = Enterprise.from_dict(profile["enterprise"])
        if 'links' in profile.keys():
            for edge_link in profile["links"]:
                links.append(Link.from_dict(edge_link))
        if 'recentLinks' in profile.keys():
            for edge_link in profile["recentLinks"]:
                recentLinks.append(Link.from_dict(edge_link))
        if 'site' in profile.keys():
            site = Site.from_dict(profile["site"])

        return cls(
            activationKey=profile.get("activationKey"),
            activationKeyExpires=activationKeyExpires,
            activationState=ActivationState(profile.get("activationState")),
            activationTime=activationTime,
            alertsEnabled=profile.get("alertsEnabled"),
            buildNumber=profile.get("buildNumber"),
            created=created,
            customInfo=profile.get("customInfo"),
            description=profile.get("description"),
            deviceFamily=profile.get("deviceFamily"),
            deviceId=profile.get("deviceId"),
            dnsName=profile.get("dnsName"),
            edgeState=profile.get("edgeState"),
            edgeStateTime=edgeStateTime,
            endpointPkiMode=EndpointPkiMode(profile.get('endpointPkiMode')),
            enterpriseId=profile.get('enterpriseId'),
            factorySoftwareVersion=profile.get('factorySoftwareVersion'),
            factoryBuildNumber=profile.get('factoryBuildNumber'),
            haLastContact=haLastContact,
            haPreviousState=str(profile["haPreviousState"]) if profile["haPreviousState"] else None,
            haSerialNumber=str(profile["haSerialNumber"]) if profile["haSerialNumber"] else None,
            haState=HaState(profile.get('haState')),
            id=(profile.get('id')),
            isLive=profile.get("isLive"),
            lastContact=lastContact,
            logicalId=profile.get("logicalId"),
            modelNumber=profile.get("modelNumber"),
            modified=modified,
            name=profile.get("name"),
            operatorAlertsEnabled=profile.get("operatorAlertsEnabled"),
            selfMacAddress=profile.get("selfMacAddress"),
            serialNumber=profile.get("serialNumber"),
            serviceState=ServiceState(profile.get('serviceState')),
            serviceUpSince=serviceUpSince,
            siteId=profile.get("siteId"),
            softwareUpdated=softwareUpdated,
            softwareVersion=profile.get("softwareVersion"),
            systemUpSince=systemUpSince,
            configuration=configuration,
            enterprise=enterprise,
            links=links,
            recentLinks=recentLinks,
            site=site
        )

    async def reactivate(self, session: VCO) -> EdgeRequestReactivationResult:
        """Request Reactivation (v4.2.1)

        Requests a new activation key and updates the Edge state to REACTIVATION_PENDING.

        Args:
            session (VCO): A Velocloud Orchestrator Session

        Returns:
            EdgeRequestReactivationResult: New Activation Key & Expiration Date
        """
        ENDPOINT = f'{BASE_ENDPOINT}/edgeRequestReactivation'
        BODY = {"enterpriseId": self.enterpriseId, "edgeId": self.id}
        RESULTS = None

        LOGGER.info(f'{self.name} [{self.id}]: Requesting reactivation.')

        data = await orchestrator.send(session=session, endpoint=ENDPOINT, body=BODY)

        RESULTS = EdgeRequestReactivationResult(
            activationKey=data.get("activationKey"),
            activationKeyExpires=datetime.strptime(data.get("activationKeyExpires"), "%Y-%m-%dT%H:%M:%S.%fZ")
        )

        self.activationKey = RESULTS.activationKey
        self.activationKeyExpires = RESULTS.activationKeyExpires

        return RESULTS

    async def cancel_reactivation(self, session: VCO) -> EdgeCancelReactivationResult:
        """Cancel Reactivation

        Removes the reactivation key and resets the edge state from PENDING_REACTIVATION

        Args:
            session (VCO): Velocloud Orchestrator session

        Returns:
            EdgeCancelReactivationResult: Rows & Errors (if applicable)
        """
        ENDPOINT = f'{BASE_ENDPOINT}/edgeCancelReactivation'
        BODY = {"enterpriseId": self.enterpriseId, "edgeId": self.id}

        LOGGER.info(f'{self.name} [{self.id}]: Cancelling reactivation request.')

        data = await orchestrator.send(session=session, endpoint=ENDPOINT, body=BODY)

        return EdgeCancelReactivationResult(rows=data.get("rows"), error=data.get("error"))

    async def delete(self, session: VCO) -> EdgeDeleteEdgeResultItem:
        """Delete Edge (untested)

        WARNING: Removes the Edge completely.

        Args:
            session (VCO): Velocloud Orchestrator session

        Returns:
            tuple: Edge ID (int), status (bool)
        """
        ENDPOINT = f'{BASE_ENDPOINT}/deleteEdge'
        BODY = {
            "enterpriseId": self.enterpriseId,
            "id": self.id
        }

        LOGGER.info(f'{self.name} [{self.id}]: Removing edge...')

        data = await orchestrator.send(session=session, endpoint=ENDPOINT, body=BODY)
        return EdgeDeleteEdgeResultItem(
            data[0].get('rows'),
            data[0].get('id'),
            data[0].get('error')
        )

    async def delete_bgp_neighbor_records(self, session: VCO):
        return None

    async def get_client_visibility_mode(self, session: VCO) -> EdgeClientVisibilityModeResult:
        """Get Client Visibility Mode"""
        ENDPOINT = ""
        BODY = {}

        LOGGER.INFO(f'{self.name} [{self.id}]: Getting client visibility mode.')

        data = await orchestrator.send(session=session, endpoint=ENDPOINT, body=BODY)

        return EdgeClientVisibilityModeResult(EdgeClientVisibilityMode(data.get("edgeClientVisibilityMode")))

    async def get_edge_configuration_modules(self, session: VCO, modules: list) -> EdgeConfigurationModulesResult:
        """Get Edge Configuration Modules"""
        # This needs to be rewritten, the whole thing (including EdgeConfigurationModulesResult)
        return None

    async def get_edge_configuration_stack(self, session: VCO) -> EdgeConfigurationStackResult:
        """Get Edge Configuration Stack
        Gets the complete configuration profile (including all modules).
        """
        # This needs to be rewritten, the whole thing (including EdgeConfigurationStackResult)
        return None

    async def get_edge_sdwan_peers(self, session: VCO, filters: dict, interval: dict) -> EdgeSdwanPeersResult:
        """Get Edge SDWAN Peers
        Get's the SD-WAN peers that have established paths.int

        (Optional) use a filter object to limit the number of SD-WAN peers returned.
        (Optional) specify a time interval with an interval object [default: current date]
        """
        # This needs to be rewritten, the whole thing (including EdgeConfigurationStackResult)
        # Filters & Interval are custom objects, the API docs are blank for these
        return None

    async def set_edge_enterprise_configuration(self, session: VCO):
        return None

    async def set_edge_handoff_gateways(self, session: VCO):
        # is handoff one word?  i think so
        return None

    async def set_edge_operator_configuration(self, session: VCO):
        return None

    async def unset_edge_operator_configuration(self, session: VCO):
        return None

    async def update_edge_admin_password(self, session: VCO):
        return None

    async def update_edge_attributes(self, session: VCO):
        return None

    async def update_edge_credentials_by_configuration(self, session: VCO):
        return None

    @staticmethod
    async def delete_edges(session: VCO, enterpriseId: int, edgeIds: list) -> list:
        """Delete All Edges (untested)

        WARNING: This will be depracated in a future update.
        WARNING: This will remove all the edges supplied from VCO.
        INFO: Static Method

        Args:
            session (VCO): Velocloud Session Object
            enterpriseId (int): Enterprise ID
            edgeIds (list): A list of Edge ID's as int

        Returns:
            list(EdgeDeleteEdgeResultItem): A list of EdgeDeleteEdgeResultItem's
        """
        ENDPOINT = f'{BASE_ENDPOINT}/deleteEdge'
        BODY = {
            "enterpriseId": enterpriseId,
            "ids": edgeIds
        }
        RESULTS = []

        LOGGER.info(f'[{enterpriseId}] Removing Edges: {edgeIds}')

        data = await orchestrator.send(session=session, endpoint=ENDPOINT, body=BODY)

        for result in data:
            RESULTS.append(
                EdgeDeleteEdgeResultItem(
                    rows=result.get('rows'),
                    id=result.get('id'),
                    error=result.get('error')
                )
            )
        return RESULTS

    @staticmethod
    async def getEdge(session: VCO, name: str, extras: list = None):
        """Get Edge

        WARNING: Refactor with new velocloud.orchestrator methods

        Args:
            session (VCO): A Velocloud Orchestrator Session object
            name (str): The specified edge name
            **kwargs:
                with (list): Optional - recentLinks, links, serviceGroups, site, enterprise, configuration, configurationWithModules

        Returns:
            Edge: An edge object
        """
        ENDPOINT = f'{BASE_ENDPOINT}/getEdge'
        BODY = {"name": name}
        BODY["with"] = extras if extras is not None else None

        data = await orchestrator.send(session=session, endpoint=ENDPOINT, body=BODY)
        return Edge.from_dict(data)

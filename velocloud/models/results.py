from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List
from velocloud.models.application import Application, ApplicationMetadata
from velocloud.models.configuration import ConfigurationModule, ConfigurationModuleName, ConfigurationModuleType, ConfigurationType, ModelConfiguration
from velocloud.models.disaster_recovery import DRClientContact
from velocloud.models.edge import ActivationState, EdgeState, EndpointPkiMode, HaState, Link, ServiceState, Site
from velocloud.models.enterprise import Enterprise, EnterpriseAlertNotification, EnterpriseAlertNotificationUserData


"""
    DATACLASSES (Configuration)
"""


@dataclass
class ConfigurationResult:
    """
    Not sure if worth documenting this...
    API Calls that use this:
        configuration_clone_configuration_result
        configuration_clone_and_convert_configuration_result
        configuration_clone_enterprise_template_result
    """
    _id: int

    def __repr__(self):
        return str(type(self))

    @property
    def configuration_id(self):
        return self._id


@dataclass
class DeleteConfigurationResult(ConfigurationResult):
    """
        configuration_delete_configuration_result
    """
    rows: dict
    error: str = None


@dataclass
class UpdateConfigurationResult:
    rows: int
    error: str = None


@dataclass
class GetConfigurationModulesResultItem(ConfigurationResult):
    """
        configuration_get_configuration_modules_result_item
    """
    name: ConfigurationModuleName
    type: ConfigurationModuleType
    description: str
    configurationid: int
    data: dict
    refs: dict
    created: datetime = None
    effective: datetime = None
    modified: datetime = None
    schemaVersion: str = None
    version: str = None
    metadata: dict = field(default_factory=dict)


@dataclass
class GetConfigurationResult(ConfigurationResult):
    """
        configuration_get_configuration_result
    """
    created: datetime
    description: str
    effective: datetime
    modified: datetime
    name: str
    version: str
    configurationType: ConfigurationType = None
    edgeCount = int = None
    logicalId: str = None
    modules: List[ConfigurationModule] = field(default_factory=list)
    schemaVersion: str = None
    isStaging: int = None


@dataclass
class GetIdentifieableApplicaitonsResults:
    applicationClassToApplication: dict
    applicationToApplicationClass: dict
    applicationClasses: str
    applications: List[Application]


@dataclass
class GetRoutableApplicationsResult(GetIdentifieableApplicaitonsResults):
    metaData: ApplicationMetadata


@dataclass
class GetDefaultApplicationsResult:
    label: str
    value: int


"""
    DATACLASSES (Disaster Recovery)
"""


class DRState(Enum):
    UNCONFIGURED = "UNCONFIGURED"
    ACTIVE_CONFIGURING = "ACTIVE_CONFIGURING"
    ACTIVE_CONFIGURED = "ACTIVE_CONFIGURED"
    ACTIVE_UNCONFIG = "ACTIVE_UNCONFIG"
    LAUNCHING_STANDBY = "LAUNCHING_STANDBY"
    LAUNCHED_STANDBY = "LAUNCHED_STANDBY"
    ACTIVE_WAIT_STANDBY = "ACTIVE_WAIT_STANDBY"
    PENDING_STANDBY_CANDIDATE = "PENDING_STANDBY_CANDIDATE"
    STANDBY_CANDIDATE = "STANDBY_CANDIDATE"
    STANDBY_CONFIG_RQST = "STANDBY_CONFIG_RQST"
    STANDBY_CONFIGURING = "STANDBY_CONFIGURING"
    STANDBY_CONFIGURED = "STANDBY_CONFIGURED"
    PENDING_STANDBY_UNCONFIG = "PENDING_STANDBY_UNCONFIG"
    STANDBY_UNCONFIG = "STANDBY_UNCONFIG"
    PENDING_STANDBY_PROMOTION = "PENDING_STANDBY_PROMOTION"
    STANDBY_PROMOTED = "STANDBY_PROMOTED"
    PENDING_ACTIVE_DEMOTION = "PENDING_ACTIVE_DEMOTION"
    COPYING_DB = "COPYING_DB"
    COPY_DB_DONE = "COPY_DB_DONE"
    COPYING_FILES = "COPYING_FILES"
    COPY_FILES_DONE = "COPY_FILES_DONE"
    SYNC_CONFIGURING = "SYNC_CONFIGURING"
    STANDBY_SYNC = "STANDBY_SYNC"
    STANDBY_BACKGROUND_IMPORT = "STANDBY_BACKGROUND_IMPORT"
    STANDBY_BACKGROUND_IMPORT_DONE = "STANDBY_BACKGROUND_IMPORT_DONE"
    STANDBY_DATA_MIGRATION = "STANDBY_DATA_MIGRATION"
    STANDBY_DATA_MIGRATION_DONE = "STANDBY_DATA_MIGRATION_DONE"
    STANDBY_DATA_MIGRATION_IN_PROGRESS = "STANDBY_DATA_MIGRATION_IN_PROGRESS"
    STANDBY_RUNNING = "STANDBY_RUNNING"
    UPGRADING = "UPGRADING"
    FAILURE_ACTIVE_CONFIGURING = "FAILURE_ACTIVE_CONFIGURING"
    FAILURE_LAUNCHING_STANDBY = "FAILURE_LAUNCHING_STANDBY"
    FAILURE_STANDBY_CONFIGURING = "FAILURE_STANDBY_CONFIGURING"
    FAILURE_GET_STANDBY_CONFIG = "FAILURE_GET_STANDBY_CONFIG"
    FAILURE_COPYING_DB = "FAILURE_COPYING_DB"
    FAILURE_COPYING_FILES = "FAILURE_COPYING_FILES"
    FAILURE_SYNC_CONFIGURING = "FAILURE_SYNC_CONFIGURING"
    FAILURE_BACKGROUND_IMPORT = "FAILURE_BACKGROUND_IMPORT"
    FAILURE_DATA_MIGRATION = "FAILURE_DATA_MIGRATION"
    FAILURE_SYNCING_FILES = "FAILURE_SYNCING_FILES"
    FAILURE_GET_STANDBY_STATUS = "FAILURE_GET_STANDBY_STATUS"
    FAILURE_GET_ACTIVE_STATUS = "FAILURE_GET_ACTIVE_STATUS"
    FAILURE_MYSQL_ACTIVE_STATUS = "FAILURE_MYSQL_ACTIVE_STATUS"
    FAILURE_MYSQL_STANDBY_STATUS = "FAILURE_MYSQL_STANDBY_STATUS"
    FAILURE_STANDBY_CANDIDATE = "FAILURE_STANDBY_CANDIDATE"
    FAILURE_STANDBY_UNCONFIG = "FAILURE_STANDBY_UNCONFIG"
    FAILURE_STANDBY_PROMOTION = "FAILURE_STANDBY_PROMOTION"
    FAILURE_ACTIVE_DEMOTION = "FAILURE_ACTIVE_DEMOTION"


class DRRole(Enum):
    STANDALONE = "STANDALONE"
    ACTIVE = "ACTIVE"
    STANDBY = "STANDBY"
    ZOMBIE = "ZOMBIE"


@dataclass
class DROperationalResult:
    rows: int
    error: str = None


@dataclass
class DRConfigureActiveForReplicationResult:
    rows: int
    error: str = None


@dataclass
class DRDemoteActiveResult:
    rows: int
    error: str = None


@dataclass
class DRGetReplicationBlobResult:
    activeAccessFromStandby: str


@dataclass
class DRGetReplicationStatusResult:
    activeAddress: str
    drState: DRState
    drVCOUser: str
    failureDescription: str
    role: DRRole
    roleTimestamp: datetime
    standbyList: list
    vcoIp: str
    vcoUuid: str
    stateHistory: list
    stateTimestamp: datetime = None
    vcoReplicationIp: str = None
    activeReplicationAddress: str = None
    clientContact: List[DRClientContact] = field(default_factory=list)
    clientCount: dict = {
        'edgeCount': None,
        'gatewayCount': None,
        'currentActiveEdgeCount': None,
        'currentStandbyEdgeCount': None,
        'currentActiveGatewayCount': None,
        'currentStandbyGatewayCount': None
    }
    lastDrProtectedTime: datetime = None


@dataclass
class DRPrepareForStandbyResult:
    rows: int
    error: str = None


@dataclass
class DRPromoteStandbyToActiveResult:
    rows: int
    error: str = None


@dataclass
class DRRemoveStandbyResult:
    rows: int
    error: str = None


@dataclass
class DRTransitionToStandbyResult:
    rows: int
    error: str = None


"""
    DATACLASSES (Edge)
"""


@dataclass
class EdgeDeleteEdgeBGPNeighborRecordsResult:
    rows: int
    id: int = None
    error: str = None


@dataclass
class EdgeDeleteEdgeResultItem:
    rows: int
    id: int = None
    error: str = None


@dataclass
class EdgeCancelReactivationResult:
    rows: int
    error: str = None


@dataclass
class EdgeProvisionResult:
    id: int
    activationKey: str
    generatedCertificate: dict = {
        'certificate': None,
        'ca-certificate': None,
        'privateKey': None,
        'privateKeyPassword': None,
        'csr': None
    }


@dataclass
class EdgeRequestReactivationResult:
    activationKey: str
    activationKeyExpires: datetime


@dataclass
class EdgeGetEdgeConfigurationStackResultItem:
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
class EdgeGetEdgeResult:
    activationkey: str
    activationkeyExpires: str
    activationState: ActivationState
    activationTime: str
    alertsEnabled: int
    buildNumber: str
    created: str
    customInfo: str
    description: str
    deviceFamily: str
    deviceId: str
    dnsName: str
    edgeState: EdgeState
    edgeStateTime: str
    endpointPkiMode: EndpointPkiMode
    enterpriseId: int
    haLastContact: str
    haPreviousState: HaState
    haSerialNumber: str
    haState: HaState
    id: int
    isLive: int
    lastContact: str
    logicalId: str
    modelNumber: str
    modified: str
    name: str
    operatorAlertsEnabled: int
    selfMacAddress: str
    serialNumber: str
    serviceState: ServiceState
    serviceUpSince: str
    siteId: int
    softwareUpdated: str
    softwareVersion: str
    systemUpSince: str
    configuration: ModelConfiguration = None
    enterprise: Enterprise = None
    links: List[Link] = None
    recentLinks: List[Link] = None
    site: Site = None


@dataclass
class EdgeSetEdgeHandOffGatewaysResult:
    rows: int
    error: str = None


@dataclass
class EdgeUpdateEdgeAdminPasswordResult:
    id: int


@dataclass
class EdgeUpdateEdgeAttributesResult:
    rows: int
    error: str = None


@dataclass
class EdgeUpdateEdgeCredentialsByConfigurationResult:
    actionIds: List[int]


@dataclass
class EdgeSetEdgeOperatorConfigurationResult:
    rows: int
    id: int = None
    error: str = None


@dataclass
class EdgeUnsetEdgeOperatorConfigurationResult:
    rows: int
    id: int = None
    error: str = None


@dataclass
class EdgeSetEnterpriseOperatorConfigurationResult:
    rows: int
    id: int = None
    error: str = None


@dataclass
class EdgeSetEdgeEnterpriseConfigurationResult:
    rows: int
    id: int = None
    error: str = None


"""
    DATACLASSES (Enterprise)
"""


class Entity(Enum):
    ACTIVE_VCO = "ACTIVE_VCO"
    STANDBY_VCO = "STANDBY_VCO"
    GATEWAY = "GATEWAY"
    DATACENTER = "DATACENTER"


class Alert(Enum):
    EDGE_DOWN = "EDGE_DOWN"
    EDGE_UP = "EDGE_UP"
    LINK_DOWN = "LINK_DOWN"
    LINK_UP = "LINK_UP"
    VPN_TUNNEL_DOWN = "VPN_TUNNEL_DOWN"
    EDGE_HA_FAILOVER = "EDGE_HA_FAILOVER"
    EDGE_SERVICE_DOWN = "EDGE_SERVICE_DOWN"
    GATEWAY_SERVICE_DOWN = "GATEWAY_SERVICE_DOWN"
    VNF_VM_EVENT = "VNF_VM_EVENT"
    VNF_VM_DEPLOYED = "VNF_VM_DEPLOYED"
    VNF_VM_POWERED_ON = "VNF_VM_POWERED_ON"
    VNF_VM_POWERED_OFF = "VNF_VM_POWERED_OFF"
    VNF_VM_DEPLOYED_AND_POWERED_OFF = "VNF_VM_DEPLOYED_AND_POWERED_OFF"
    VNF_VM_DELETED = "VNF_VM_DELETED"
    VNF_VM_ERROR = "VNF_VM_ERROR"
    VNF_INSERTION_EVENT = "VNF_INSERTION_EVENT"
    VNF_INSERTION_ENABLED = "VNF_INSERTION_ENABLED"
    VNF_INSERTION_DISABLED = "VNF_INSERTION_DISABLED"
    TEST_ALERT = "TEST_ALERT"
    EDGE_CSS_TUNNEL_DOWN = "EDGE_CSS_TUNNEL_DOWN"
    EDGE_CSS_TUNNEL_UP = "EDGE_CSS_TUNNEL_UP"
    NVS_FROM_EDGE_TUNNEL_DOWN = "NVS_FROM_EDGE_TUNNEL_DOWN"
    NVS_FROM_EDGE_TUNNEL_UP = "NVS_FROM_EDGE_TUNNEL_UP"
    VNF_IMAGE_DOWNLOAD_EVENT = "VNF_IMAGE_DOWNLOAD_EVENT"
    VNF_IMAGE_DOWNLOAD_IN_PROGRESS = "VNF_IMAGE_DOWNLOAD_IN_PROGRESS"
    VNF_IMAGE_DOWNLOAD_COMPLETED = "VNF_IMAGE_DOWNLOAD_COMPLETED"
    VNF_IMAGE_DOWNLOAD_FAILED = "VNF_IMAGE_DOWNLOAD_FAILED"


class AlertState(Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"


class AnalyticsCapability(Enum):
    NONE = "NONE"
    APPLICATION_BRANCH = "APPLICATION_BRANCH"


@dataclass
class EnterpriseDeleteEnterpriseGatewayRecordsResult:
    rows: int
    id: int = None
    error: str = None


@dataclass
class EnterpriseDeleteEnterpriseNetworkAllocationResult:
    rows: int
    id: int = None
    error: str = None


@dataclass
class EnterpriseDeleteEnterpriseResult:
    rows: int
    id: int = None
    error: str = None


@dataclass
class EnterpriseDeleteEnterpriseServiceResult:
    rows: int
    id: int = None
    error: str = None


@dataclass
class EnterpriseGetEnterpriseAddressesResultItem:
    address: str = None
    entity: Entity = None


@dataclass
class EnterpriseGetEnterpriseAlertDefinitionsResultItem:
    id: int
    created: datetime
    name: Alert
    type: Alert
    definition: dict
    firstNotificationSeconds: int
    maxNotifications: int
    notificationIntervalSeconds: int
    resetIntervalSeconds: int
    modified: datetime


@dataclass
class EnterpriseGetEnterpriseAlertConfigurationsResultItem:
    id: int
    created: datetime
    alertDefinitionId: int
    enterpriseId: int
    enabled: bool
    name: Alert
    description: str
    type: Alert
    definition: dict
    firstNotificationSeconds: int
    maxNotifications: int
    notificaitonintervalSeconds: int
    resetIntervalSeconds: int
    modified: datetime


@dataclass
class EnterpriseGetEnterpriseAlertsResultItem:
    id: int
    created: datetime
    triggerTime: datetime
    enterpriseAlertConfigurationId: int
    enterpriseId: int
    edgeId: int
    edgeName: str
    linkId: int
    linkName: str
    enterpriseObjectId: int
    enterpriseObjectName: str
    name: Alert
    type: Alert
    state: AlertState
    stateSetTime: datetime
    lastContact: datetime
    firstNotificationSeconds: int
    maxNotifications: int
    notificationintervalSeconds: int
    resetIntervalSeconds: int
    comment: str
    nextNotificationTime: datetime
    remainingNotifications: int
    timezone: str
    locale: str
    modified: datetime
    notifications: List[EnterpriseAlertNotification] = field(default_factory=list)


@dataclass
class EnterpriseGetEnterpriseAllALertRecipientsResult:
    emailEnabled: bool
    emailList: List[str]
    enterpriseuser: List[EnterpriseAlertNotificationUserData]
    mobileenabled: bool
    mobileList: List[str]
    smsEnabled: bool
    smsList: List[str]
    snmpEnabled: bool = None
    snmpList: List[str] = None
    webhookEnabled: bool = None
    webhookList: dict = None


@dataclass
class EnterpriseGetEnterpriseCapabilitiesResult:
    edgeVnfs_enable: bool = None
    edgeVnfs_securityVnf_paloAlto: bool = None
    edgeVnfs_securityVnf_checkpoint: bool = None
    edgeVnfs_securityVnf_fortinet: bool = None
    enableCosMapping: bool = None
    enableEnterpriseAuth: bool = None
    enableFwLogs: bool = None
    enableStatefulFirewall: bool = None
    enableNetworks: bool = None
    enablePremium: bool = None
    enableSegmentation: bool = None
    enbleServiceRateLimiting: bool = None
    enableRoleCustomization: bool = None


@dataclass
class EnterpriseGetAnalyticsConfigurationResult:
    analyticsCapability: AnalyticsCapability = None
    analyticsEdgeLimit: int = None


@dataclass
class EnterpriseProxyGetEnterpriseProxyCapabilitiesResult:
    enableRoleCustomization: bool = None


@dataclass
class EnterpriseGetEnterpriseConfigurationsWithPoliciesResult:
    configurationType: ConfigurationType = None
    created: str = None
    description: str = None
    edgeCount: int = None
    effective: str = None
    id: int = None
    isStaging: int = None
    logicalId: str = None
    modified: str = None
    name: str = None
    policies: dict = None
    schemaVersion: str = None
    version: str = None


@dataclass
class EnterpriseGetEnterpriseConfigurationsResultItem:
    created: datetime
    description: str
    effective: datetime
    id: int
    modified: datetime
    name: str
    version: str
    isStaging: int
    configurationType: ConfigurationType = None
    edgeCount: int = None
    logicalId: str = None
    modules: List[ConfigurationModule] = field(default_factory=list)
    schemaVersion: str = None
    edges: List[dict] = field(default_factory=list)


@dataclass
class EnterpriseGetEnterpriseOperatorConfigurationTypeResult:
    configurationType: ConfigurationType

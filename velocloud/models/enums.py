from enum import Enum


class bgpFilterRuleAction(Enum):
    """BGP Filter Rule Action"""
    PERMIT = "PERMIT"
    DENY = "DENY"


class bgpFilterRuleMatchType(Enum):
    """BGP Filter Rule Match Type"""
    COMMUNITY = "COMMUNITY"
    PREFIX = "PREFIX"


class bgpFilterRuleValueType(Enum):
    """BGP Filter Rule Value Type"""
    AS_PATH_PREPEND = "AS_PATH_PREPEND"
    METRIC = "METRIC"
    LOCAL_PREFERENCE = "LOCAL_PREFERENCE"
    COMMUNITY = "COMMUNITY"


class BgpNeighborTag(Enum):
    """BGP Neighbor Tag"""
    UPLINK = "UPLINK"


class cellularNetwork(Enum):
    """Cellular Network"""
    ATT = "ATT"
    SPRINT = "SPRINT"
    VERIZON = "VERIZON"
    GENERIC = "GENERIC"


class cloudSecurityTunnelingProtocol(Enum):
    """Cloud Security Tunneling Protocol"""
    GRE = "GRE"
    IPSEC = "IPSEC"


class configurationModuleName(Enum):
    """Configuration Module Name"""
    imageUpdate = "imageUpdate"
    controlPlane = "controlPlane"
    managementPlane = "managementPlane"
    firewall = "firewall"
    QOS = "QOS"
    deviceSettings = "deviceSettings"
    WAN = "WAN"
    metaData = "metaData"
    properties = "properties"
    analyticsSettings = "analyticsSettings"


class configurationModuleType(Enum):
    """configuratino module type"""
    ENTERPRISE = "ENTERPRISE"
    OPERATOR = "OPERATOR"
    GATEWAY = "GATEWAY"


class configurationModuleSegmentType(Enum):
    """Configuration Module Segment Type"""
    REGULAR = "REGULAR"
    CDE = "CDE"
    PRIVATE = "PRIVATE"


class deviceSettingsMulticastPimType(Enum):
    """Device Settings - Multicast - PIM Type"""
    SOURCE_IP = "SOURCE_IP"


class deviceSettingsMulticastRpType(Enum):
    """Device Settings - Multicast - RP Type"""
    STATIC = "STATIC"


class deviceSettingsNatRuleType(Enum):
    """Device Settinsg - NAT Rule Type"""
    source = "source"
    destination = "destination"


class deviceSettingsNtpAuth(Enum):
    """Device Settings - NTP - Auth"""
    NONE = "NONE"
    MD5 = "MD5"


class deviceSettingsOspfDefaultRouteType(Enum):
    """Device Settings - OSPF Default Route Type"""
    OE1 = "OE1"
    OE2 = "OE2"
    NONE = "NONE"


class deviceSettingsOspfBgpRouteRedistributionType(Enum):
    """Device Settings - OSPF BGP Route Redistribution Type"""
    E1 = "E1"
    E2 = "E2"


class deviceSettingsOspfDefaultRouteAdvertising(Enum):
    """Device Settings - OSPF Default Route Advertising"""
    ALWAYS = "ALWAYS"
    CONDITIONAL = "CONDITIONAL"
    NONE = "NONE"


class deviceSettingsRef(Enum):
    """Device Settings - Ref"""
    deviceSettings_authentication = "deviceSettings:authentication"
    deviceSettings_css_provider = "deviceSettings:css:provider"
    deviceSettings_edgeDirectNvs_provider = "deviceSettings:edgeDirectNvs:provider"
    deviceSettings_dns_primaryProvider = "deviceSettings:dns:primaryProvider"
    deviceSettings_dns_backupProvider = "deviceSettings:dns:backupProvider"
    deviceSettings_dns_privateProviders = "deviceSettings:dns:privateProviders"
    deviceSettings_vpn_dataCenter = "deviceSettings:vpn:dataCenter"
    deviceSettings_vpn_edgeHub = "deviceSettings:vpn:edgeHub"
    deviceSettings_tacacs = "deviceSettings:tacacs"


class deviceSettingsRoutedInterfaceVsdl2Profile(Enum):
    """Device Settings - Routed Interface DSL Settings VDSL2 Profile"""
    seventeen_a = "17a"
    thirty_a = "30a"


class deviceSettingsSecurityVnfVmVendor(Enum):
    """Device Settings - Security VNF VM Vendor"""
    PaloAlto = "PaloAlto"
    CheckPoint = "CheckPoint"
    Fortinet = "Fortinet"
    CentOS = "CentOS"


class deviceSettingsSubinterfaceType(Enum):
    """Device Settings Subinterface Type"""
    SECONDARY_IP = "SECONDARY_IP"
    SUB_INTERFACE = "SUB_INTERFACE"


class deviceSettingsSyslogFacilityCode(Enum):
    """Device Settings - Syslog Facility Code"""
    local0 = "local0"
    local1 = "local1"
    local2 = "local2"
    local3 = "local3"
    local4 = "local4"
    local5 = "local5"
    local6 = "local6"
    local7 = "local7"


class deviceSettingsSyslogCollectorIpProtocol(Enum):
    """Device Settings - Syslog Collector IP Protocol"""
    TCP = "TCP"
    UDP = "UDP"


class deviceSettingsSyslogCollectorRole(Enum):
    """Device SEttings - Syslog Collector Role"""
    EDGE_EVENT = "EDGE EVENT"
    FIREWALL_EVENT = "FIREWALL EVENT"
    EDGE_AND_FIREWALL_EVENT = "EDGE AND FIREWALL EVENT"


class deviceSettingsSyslogCollectorSeverity(Enum):
    """Device Settings - Syslog Collector Severity"""
    EMERG = "EMERG"
    ALERT = "ALERT"
    CRIT = "CRIT"
    ERR = "ERR"
    WARNING = "WARNING"
    NOTICE = "NOTICE"
    INFO = "INFO"
    DEBUG = "DEBUG"


class deviceSettingsVpnType(Enum):
    """Device Settings - VPN - Type"""
    edgeHub = "edgeHub"
    edgeHubCluster = "edgeHubCluster"


class deviceSettingsVqmProtocol(Enum):
    """Device Settings - VQM Protocol"""
    RFC6035 = "RFC6035"


class deviceSettingsWanOverlay(Enum):
    """Device Settings Wan Overlay"""
    DISABLED = "DISABLED"
    AUTO_DISCOVERED = "AUTO_DISCOVERED"
    USER_DEFINED = "USER_DEFINED"


class gwDisplayTimeUnit(Enum):
    """Display Time Unit"""
    DAY = "DAY"
    HOUR = "HOUR"
    MINUTE = "MINUTE"


class dslMode(Enum):
    """DSL Mode"""
    standard = "standard"
    dsl = "dsl"
    gpon = "gpon"


class igmpType(Enum):
    """IGMP Type"""
    IGMP_V2 = "IGMP_V2"


class pimType(Enum):
    """PIM Type"""
    PIM_SM = "PIM_SM"


class lanInterfaceAuthenticationType(Enum):
    """LAN Interface Authentication Type"""
    none = "none"
    dot1x = "802.1x"  # This is probably a failure


class interfaceDuplex(Enum):
    """Interface Duplex"""
    FULL = "FULL"
    HALF = "HALF"


class lanInterfaceMode(Enum):
    """LAN Interface Mode"""
    access = "access"
    trunk = "trunk"


class lanInterfaceSecurityMode(Enum):
    """LAN Interface Security Mode"""
    Open = "Open"
    WPA2Enterprise = "WPA2Enterprise"
    WPA2Personal = "WPA2Personal"


class lanInterfaceType(Enum):
    """LAN Interface Type"""
    wired = "wired"
    wireless = "wireless"


class lanVisibilityMode(Enum):
    """LAN Visibility Mode"""
    MAC = "MAC"
    IP = "IP"


class endpointPkiMode(Enum):
    """endpointPkiMode"""
    CERTIFICATE_DISABLED: "CERTIFICATE_DISABLED"
    CERTIFICATE_OPTIONAL: "CERTIFICATE_OPTIONAL"
    CERTIFICATE_REQUIRED: "CERTIFICATE_REQUIRED"


class enterpriseAlertDefinitionNameAndType(Enum):
    """Enteerprise Alert Definition & Type"""
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


class enterpriseAlertTriggerState(Enum):
    """Enterprise Alert Trigger States"""
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"


class enterpriseNetworkSpaceMode(Enum):
    static = "static"
    dynamic = "dynamic"


class enterpriseProxyType(Enum):
    PARTNER = "PARTNER"
    MSP = "MSP"


class eventBaseCategory(Enum):
    SYSTEM = "SYSTEM"
    NETWORK = "NETWORK"
    APPLICATION = "APPLICATION"
    USER = "USER"
    SECURITY = "SECURITY"
    EDGE = "EDGE"
    GATEWAY = "GATEWAY"
    CONFIGURATION = "CONFIGURATION"
    ENTERPRISE = "ENTERPRISE"


class eventBaseSeverity(Enum):
    EMERGENCY = "EMERGENCY"
    ALERT = "ALERT"
    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    NOTICE = "NOTICE"
    INFO = "INFO"
    DEBUG = "DEBUG"


class firewallRuleActionType(Enum):
    """Firewall Action Type"""
    port_forwarding = "port_forwarding"
    one_to_one_nat = "one_to_one_nat"


class firewallRuleOutboundAction(Enum):
    """Firewall Rule Outbound Action"""
    allow = "allow"
    deny = "deny"
    drop = "drop"
    reject = "reject"
    skip = "skip"


class firewallRuleType(Enum):
    """Firewall Rule Type"""
    exact = "exact"
    prefix = "prefix"
    wildcard = "wildcard"
    netmask = "netmask"


class gatewayHandoffType(Enum):
    NAT = "NAT"
    VLAN = "VLAN"


class gatewayPoolHandoffType(Enum):
    NONE = "NONE"
    ALLOW = "ALLOW"
    ONLY = "ONLY"


class linkBackupState(Enum):
    UNCONFIGURED = "UNCONFIGURED"
    STANDBY = "STANDBY"
    ACTIVE = "ACTIVE"


class linkMetricTrafficType(Enum):
    zero = 0
    one = 1
    two = 2


class linkMetricAction(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4


class linkMetricMetric(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5


class linkMetricState(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4


class linkLinkMode(Enum):
    """Link Mode (v4.2.1)"""
    ACTIVE = "ACTIVE"
    BACKUP = "BACKUP"
    HOSTSTASNDBY = "HOSTSTANDBY"


class linkNetworkSide(Enum):
    UNKNOWN = "UNKNOWN"
    UNKOWN = "UNKOWN"  # API Typo
    WAN = "WAN"
    LAN = "LAN"


class linkNetworkType(Enum):
    UNKNOWN = "UNKNOWN"
    WIRELESS = "WIRELESS"
    ETHERNET = "ETHERNET"
    WIFI = "WIFI"


class linkServiceGroups(Enum):
    ALL = "ALL"
    PRIVATE_WIRED = "PRIVATE_WIRED"
    PUBLIC_WIRED = "PUBLIC_WIRED"
    PUBLIC_WIRELESS = "PUBLIC_WIRELESS"


class linkServiceState(Enum):
    IN_SERVICE = "IN_SERVICE"
    OUT_OF_SERVICE = "OUT_OF_SERVICE"
    PENDING_SERVICE = "PENDING_SERVICE"


class linkState(Enum):
    UNKNOWN = "UNKNOWN"
    STABLE = "STABLE"
    UNSTABLE = "UNSTABLE"
    DISCONNECTED = "DISCONNECTED"
    QUIET = "QUIET"
    INITIAL = "INITIAL"
    STANDBY = "STANDBY"


class managementPlaneName(Enum):
    """Management Plane module type"""
    imageUpdate = "imageUpdate"
    controlPlane = "controlPlane"
    managementPlane = "managementPlane"
    firewall = "firewall"
    QOS = "QOS"
    deviceSettings = "deviceSettings"
    WAN = "WAN"
    metaData = "metaData"
    properties = "properties"
    analyticsSettings = "analyticsSettings"


class managementPlaneType(Enum):
    """Management Plane module type"""
    ENTERPRISE = "ENTERPRISE"
    OPERATOR = "OPERATOR"
    GATEWAY = "GATEWAY"


class netflowFilterDataAction(Enum):
    """Netflow Filter Data Action"""
    allow = "allow"
    deny = "deny"


class netflowFilterRuleType(Enum):
    """Firewall Rule Type"""
    exact = "exact"
    prefix = "prefix"
    wildcard = "wildcard"
    netmask = "netmask"


class routedInterfaceAddressingType(Enum):
    """Routed Interfaces Addressing Type"""
    DHCP = "DHCP"
    STATIC = "STATIC"
    PPOE = "PPOE"


class routedInterfaceOspfFilterAction(Enum):
    """Routed Interface OSPF Filter Action"""
    ADVERTISE = "ADVERTISE"
    IGNORE = "IGNORE"
    LEARN = "LEARN"


class rPF(Enum):
    """RPF"""
    SPECIFIC = "SPECIFIC"
    LOOSE = "LOOSE"
    DISABLED = "DISABLED"


class ruleType(Enum):
    """Misc. Rule Type"""
    exact = "exact"
    prefix = "prefix"
    wildcard = "wildcard"
    netmask = "netmask"


class tinyint(Enum):
    """tinyint"""
    ONE = 1
    ZERO = 0


class unitName(Enum):
    """Unit Name
    This is used in various places.
    """
    imageUpdate = "imageUpdate"
    controlPlane = "controlPlane"
    managementPlane = "managementPlane"
    firewall = "firewall"
    QOS = "QOS"
    deviceSettings = "deviceSettings"
    WAN = "WAN"
    metaData = "metaData"
    properties = "properties"
    analyticsSettings = "analyticsSettings"


class unitType(Enum):
    """Unit Type
    This is used in various places.
    """
    ENTERPRISE = "ENTERPRISE"
    OPERATOR = "OPERATOR"
    GATEWAY = "GATEWAY"


class wanDataLinkDiscovery(Enum):
    """WAN Data - Link Discovery"""
    DISABLED = "DISABLED"
    AUTO_DISCOVERED = "AUTO_DISCOVERED"
    USER_DEFINED = "USER_DEFINED"


class wanDataLinkMode(Enum):
    """WAN Data - Link Mode"""
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"


class wanDataLinkType(Enum):
    """WAN Data - Link Type"""
    WIRED = "WIRED"
    WIRELESS = "WIRELESS"


class edgeDeviceSettingsWanOverlay(Enum):
    """WAN Overlay"""
    DISABLED = "DISABLED"
    AUTO_DISCOVERED = "AUTO_DISCOVERED"
    USER_DEFINED = "USER_DEFINED"


class nvsIkePropAuthenticationAlgorithm:
    Any = "Any"
    MD5 = "MD5"
    SHA_1 = "SHA_1"
    SHA_256 = "SHA_256"


class nvsIkePropEncryptionAlgorithm:
    Any = "Any"
    AES_128_CBC = "AES_128_CBC"
    AES_192_CBC = "AES_192_CBC"
    AES_256_CBC = "AES_256_CBC"
    AES_128_GCM = "AES_128_GCM"
    AES_192_GCM = "AES_192_GCM"
    AES_256_GCM = "AES_256_GCM"
    NONE = "None"


class nvsIkePropPeerIkeId:
    IPV4_ADDR = "IPV4_ADDR"
    FQDN = "FQDN"
    USER_FQDN = "USER_FQDN"


class nvsIpsecPropEncryptionAlgorithm:
    Any = "Any"
    AES_128_CBC = "AES_128_CBC"
    AES_192_CBC = "AES_192_CBC"
    AES_256_CBC = "AES_256_CBC"
    AES_128_GCM = "AES_128_GCM"
    AES_192_GCM = "AES_192_GCM"
    AES_256_GCM = "AES_256_GCM"
    NONE = "None"


class nvsIpsecPropTunnelType:
    ROUTE = "ROUTE"
    POLICY = "POLICY"


class nvsIpsecProtocol:
    ESP_AUTH = "ESP_AUTH"
    ESP_NULL = "ESP_NULL"


class nvsProvider(Enum):
    genericIKEv2Router = "genericIKEv2Router"
    genericIKEv1Router = "genericIKEv1Router"


class nvsProviderCategory(Enum):
    DATACENTER = "DATACENTER"
    CSS = "CSS"


class nvsTunnelingProtocol(Enum):
    IPSEC = "IPSEC"
    GRE = "GRE"


class nvsType(Enum):
    genericIKEv2Router = "genericIKEv2Router"
    genericIKEv1Router = "genericIKEv1Router"


class vnfVendor(Enum):
    PaloAlto = "PaloAlto"
    CheckPoint = "CheckPoint"
    Fortinet = "Fortinet"
    CentOS = "CentOS"


class vnfDownloadType(Enum):
    s3 = "s3"
    http = "http"
    https = "https"


class vnfDownloadStatus(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    ERROR = "ERROR"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    UNKNOWN = "UNKNOWN"

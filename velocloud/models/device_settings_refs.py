from dataclasses import dataclass


@dataclass
class WebProxy:
    """Web Proxy
    This is a custom class.
    """
    provider: dict = None


@dataclass
class Vpn:
    """VPN
    This is a custom class.
    """
    dataCenter: dict = None
    edgeHub: dict = None
    edgeHubCluster: dict = None


@dataclass
class Vnfs:
    """VNFS
    This is a custom class.
    """
    edge: dict = None
    vnfImage: dict = None


@dataclass
class Segment:
    """Segment
    This is a custom class.
    """
    netflowCollectors: dict = None
    netflowFilters: dict = None


@dataclass
class SecurityVnf:
    """Security VNF
    This is a custom class.
    """
    license: dict = None
    service: dict = None


@dataclass
class Lan:
    """LAN
    This is a custom class.
    """
    allocation: dict = None


@dataclass
class HandOffGateways:
    """Hand Off Gateways
    This is a custom class.
    """
    gateways: dict = None


@dataclass
class Dns:
    """DNS
    This is a custom class.
    """
    backupProvider: dict = None
    primaryProvider: dict = None
    privateProviders: dict = None


@dataclass
class EdgeDirectNvs:
    """Edge Direct NVS
    This is a custom  class.
    """
    provider: dict = None
    site: dict = None


@dataclass
class Css:
    """CSS
    This is a custom class.
    """
    provider: dict = None
    site: dict = None


@dataclass
class DeviceSettings:
    """Device Settings
    This is a custom class.
    """
    authentication: dict = None
    css: Css = None
    edgeDiredctNvs = EdgeDirectNvs = None
    dns: Dns = None
    handOffGateways: HandOffGateways = None
    lan = Lan = None
    securityVnf = SecurityVnf = None
    segment: Segment = None
    tacacs: dict = None
    vnfs: Vnfs = None
    vpn: Vpn = None
    webProxy: WebProxy = None


@dataclass
class DeviceSettingsRefs:
    """Device Settings Refs"""
    deviceSettings: DeviceSettings = None

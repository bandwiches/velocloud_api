from dataclasses import dataclass


@dataclass
class SecurityVnf:
    """Security VNF
    This is a custom class.
    """
    paloAlto: bool = None
    checkpoint: bool = None
    fortinet: bool = None


@dataclass
class EdgeVnfs:
    """Edge VNFS
    This is a custom class.
    """
    enable: bool = None
    securityVnf: SecurityVnf = None


@dataclass
class EnterpriseGetEnterpriseCapabilitiesResult:
    """Enterprise Get Enterprise Capabilities Result"""
    edgeVnfs: EdgeVnfs
    enableCosMapping: bool = None
    enableEnterpriseAuth: bool = None
    enableFwLogs: bool = None
    enableStatefulFirewall: bool = None
    enableNetworks: bool = None
    enablePremium: bool = None
    enableSegmentation: bool = None
    enableServiceRateLimiting: bool = None
    enableRoleCustomization: bool = None

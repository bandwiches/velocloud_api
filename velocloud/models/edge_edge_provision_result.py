from dataclasses import dataclass


@dataclass
class GeneratedCertificate:
    """Generated Certificate
    This is a custom class.
    """
    certificate: str = None
    ca_certificate: str = None
    privateKey: str = None
    privateKeyPassword: str = None
    csr: str = None


@dataclass
class EdgeEdgeProvisionResult:
    """Edge Edge Provision Result"""
    id: int
    activationKey: str
    generatedCertificate: GeneratedCertificate = None

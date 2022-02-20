from dataclasses import dataclass
from datetime import datetime


@dataclass
class GatewayCertificate:
    """Gateway Certificate"""
    id: int = None
    created: datetime = None
    csrId: int = None
    gatewayId: int = None
    networkId: int = None
    certificate: str = None
    serialNumber: str = None
    subjectKeyId: str = None
    fingerPrint: str = None
    fingerPrint256: str = None
    validFrom: datetime = None
    validTo: datetime = None

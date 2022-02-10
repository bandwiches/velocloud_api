from dataclasses import dataclass
from datetime import datetime


@dataclass
class EdgeCertificate:
    """Edge Certificate"""
    id: int = None
    created: datetime = None  # datetime
    csrId: int = None
    edgeId: int = None
    enterpriseId: int = None
    certificate: str = None
    serialNumber: str = None
    subjectKeyId: str = None
    fingerPrint: str = None
    fingerPrint256: str = None
    validFrom: datetime = None  # datetime
    validTo: datetime = None  # datetime

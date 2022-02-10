from dataclasses import dataclass
from datetime import datetime


@dataclass
class EdgeEdgeRequestReactivationResult:
    """Edge Edge Requested Reactivation Result"""
    activationKey: str
    activationKeyExpires: datetime  # datetime

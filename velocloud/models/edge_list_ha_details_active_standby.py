from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import edgeHaState


@dataclass
class EdgeListHaDetailsActiveStandby:
    """Edge List HA Details Active/Standby"""
    haLastContact: datetime  # Datetime
    haPreviousState: edgeHaState
    haSerialNumber: str
    haState: edgeHaState

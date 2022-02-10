from dataclasses import dataclass


@dataclass
class DisasterRecoveryPrepareForStandbyResult:
    """Disaster Recovery Prepare for Standby Result

    Properties:
        error (str): An error message explaining why the method failed
        rows (int): The number of rows modified
    """
    rows: int
    error: str = None

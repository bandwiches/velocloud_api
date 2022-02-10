from dataclasses import dataclass


@dataclass
class DisasterRecoveryRemoveStandbyResult:
    """Disaster Recovery Remove Standby Result

    Properties:
        error (str): An error message explaining why the method failed
        rows (int): The number of rows modified
    """
    rows: int
    error: str = None

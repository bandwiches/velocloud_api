from dataclasses import dataclass


@dataclass
class EdgeEdgeCancelReactivationResultItem:
    """Edge Edge Cancel Reactivation Result Item

    Properties
        error (str): An error message explaining why the method failed
        rows (int): The number of rows modified
    """
    rows: int
    error: str = None

from dataclasses import dataclass


@dataclass
class EdgeDeleteEdgeBgpNeighborRecordsResult:
    """Edge Delete Edge BGP Neighbor Records Result

    Properties
        id (int): The id of the deleted object.
        error (str): An error message explaining why the method failed
        rows (int): The number of rows modified
    """
    rows: int
    id: int = None
    error: str = None

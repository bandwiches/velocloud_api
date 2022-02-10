from dataclasses import dataclass


@dataclass
class EdgeUnsetEdgeOperatorConfigurationResult:
    """Edge UnSet Edge Operator Configuration Result

    Properties:
        id (int):  The id of the newly-created object.
        error (str): An error message explaining why the method failed
        rows (int): The number of rows modified
    """
    rows: int
    id: int = None
    error: str = None

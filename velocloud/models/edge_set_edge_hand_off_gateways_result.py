from dataclasses import dataclass


@dataclass
class EdgeSetEdgeHandOffGatewaysResult:
    """Edge Set Edge Hand Off Gateways Result

    Properties:
        error (str): An error message explaining why the method failed
        rows (int): The number of rows modified
    """
    rows: int
    error: str = None

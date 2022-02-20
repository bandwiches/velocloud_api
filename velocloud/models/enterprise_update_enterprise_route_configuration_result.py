from dataclasses import dataclass


@dataclass
class EnterpriseUpdateEnterpriseRouteConfigurationResult:
    """Enterprise Update Enterprise Route Configuration Result

    Args:
        rows (int): The number of rows modified.
        error (str): An error message explaining why the method failed
    """
    rows: int
    error: str = None

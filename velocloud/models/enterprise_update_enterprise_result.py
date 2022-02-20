from dataclasses import dataclass


@dataclass
class EnterpriseUpdateEnterpriseResult:
    """Enterprise Update Enterprise Result

    Args:
        rows (int): The number of rows modified.
        error (str): An error message explaining why the method failed.
    """
    rows: str
    error: str = None

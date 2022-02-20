from dataclasses import dataclass


@dataclass
class EnterpriseProxyInsertEnterpriseProxyEnterpriseResult:
    """Enterprise Proxy Insert Enterprise Proxy Enterprise Result

    Args:
        id (int): The id of the newly-created object.
        rows (int): The number of rows modified.
        error (str): An error message explaining why the method failed.
    """
    rows: str
    id: int = None
    error: str = None

from dataclasses import dataclass


@dataclass
class EnterpriseDeleteEnterpriseGatewayRecordsResult:
    """Enterprise Delete Enterprise Gateway Records Result

    Properties:
        id (int):  The id of the newly-created object.
        error (str): An error message explaining why the method failed
        rows (int): The number of rows modified
    """
    rows: int
    id: int = None
    error: str = None

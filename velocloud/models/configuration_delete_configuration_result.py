from dataclasses import dataclass


@dataclass
class ConfigurationDeleteConfigurationResult:
    """Configuration Delete Configuration Result

    Properties:
        rows (int): The number of rows modified
        id (int): The ID of the deleted object.
        error (str): An error message explaining why the method failed
    """
    rows: int
    id: int = None
    error: str = None

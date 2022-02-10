from dataclasses import dataclass


@dataclass
class ConfigurationuUpdateConfigurationModuleResult:
    """Configuration Update Configuration Module Result

    Properties:
        rows (int): An error message explaining why the method failed
        errore (str): The number of rows modified

    """
    rows: int
    error: str = None

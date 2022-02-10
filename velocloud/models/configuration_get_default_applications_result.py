from dataclasses import dataclass


@dataclass
class ConfigurationGetDefaultApplicationsResult:
    """Configuration Get Default Applications Result

    Properties:
        label (str): Name of an application
        value (int): ID of an application

    """
    label: str
    value: int

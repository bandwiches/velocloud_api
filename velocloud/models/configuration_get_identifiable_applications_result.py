from dataclasses import dataclass
from typing import List
from velocloud.models.application import Application


@dataclass
class ApplicationClassToApplication:
    """Application Class to Application
    This is a custom class.
    """
    data: int = None


@dataclass
class ApplicationToApplicationClass:
    """Application Class to Application
    This is a custom class.
    """
    data: int = None


@dataclass
class ConfigurationGetIdentifiableApplicationsResult:
    """Configuration Get Identifiable Applications Result

    Parameters:
        applicationClassToApplication (Map): Maps application class IDs (strings) to application IDs (integers)
        applicationToApplicationClass (Map): Maps application IDs (strings) to class IDs (integers)
        applicationClasses (str): Map of application class IDs to class names

    """
    applicationClassToApplication: ApplicationClassToApplication
    applicationToApplicationClass: ApplicationToApplicationClass
    applicationClasses: str  # additionalProperties: OrderedMap { "type": "integer" }
    applications: List(Application)

from dataclasses import dataclass


@dataclass
class Application:
    """Application
    This is a custom class.
    """
    logicalId: str = None
    type: str = None
    version: str = None


@dataclass
class MetadataData:
    """Metadata Data"""
    applications: Application = None

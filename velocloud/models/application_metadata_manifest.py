from dataclasses import dataclass


@dataclass
class ApplicationMetadataManifest:
    """Application Metadata Manifest"""
    description: str
    name: str
    version: str

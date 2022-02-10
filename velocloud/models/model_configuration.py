from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from velocloud.models.enums import configurationModelType, tinyint
from velocloud.models.configuration_module import ConfigurationModule


@dataclass
class ModelConfiguration:
    """Model Configuration"""
    configurationType: configurationModelType = None
    created: datetime = None  # datetime
    description: str = None
    edgeCount: int = None
    effective: datetime = None  # datetime
    id: int = None
    logicalId: str = None
    modified: datetime = None  # datetime
    modules: List(ConfigurationModule) = field(default_factory=list)
    name: str = None
    schemaVersion: str = None
    version: str = None
    isStaging: tinyint = None

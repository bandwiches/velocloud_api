from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from velocloud.models.enums import configurationModelType, tinyint
from velocloud.models.configuration_module import ConfigurationModule


@dataclass
class ConfigurationGetConfigurationResult:
    """Configuration Get Configuration Result"""
    created: datetime  # datetime
    description: str
    effective: datetime  # datetime
    id: int
    modified: datetime  # datetime
    name: str
    version: str
    configurationType: configurationModelType = None
    edgeCount: int = None
    logicalId: str = None
    modules: List(ConfigurationModule) = field(default_factory=list)
    schemaVersion: str = None
    isStaging: tinyint = None

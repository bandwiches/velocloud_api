from dataclasses import dataclass
from datetime import datetime
from typing import List
from velocloud.models.enums import configurationModelType, tinyint
from velocloud.models.configuration_module import ConfigurationModule


@dataclass
class EdgeGetEdgeConfigurationStackResultItem:
    """Edge Get Edge Configuration Stack Result Item"""
    created: datetime  # datetime
    description: str
    id: int
    modified: datetime
    modules: List(ConfigurationModule)
    name: str
    version: str
    configurationType: configurationModelType = None
    edgeCount: int = None
    effective: datetime = None  # datetime
    logicalId: str = None
    schemaVersion: str = None
    isStaging: tinyint = None

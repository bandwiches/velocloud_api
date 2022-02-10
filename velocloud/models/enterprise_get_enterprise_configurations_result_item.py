from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from velocloud.models.enums import configurationModuleType, edgeActivationState, tinyint
from velocloud.models.configuration_module import ConfigurationModule


@dataclass
class Edge:
    """Edge
    This is a custom class.
    """
    name: str = None
    buildNumber: str = None
    softwareVersion: str = None
    modelNumber: str = None
    activationState: edgeActivationState = None
    logicalId: str = None
    id: int = None
    lastContact: str = None


@dataclass
class EnterpriseGetEnterpriseConfigurationsResultItem:
    """Enterprise Get Enterprise Configuration Result Item"""
    created: datetime  # datetime
    description: str
    effective: datetime  # datetime
    id: int
    logicalId: str
    modified: datetime  # datetime
    name: str
    version: str
    isStaging: tinyint
    configurationType: configurationModuleType = None
    edgeCount: int = None
    modules: List(ConfigurationModule) = field(default_factory=list)
    schemaVersion: str = None
    edges: List(Edge) = field(default_factory=list)

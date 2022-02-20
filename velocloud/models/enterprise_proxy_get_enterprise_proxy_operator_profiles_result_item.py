from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from velocloud.models.enums import configurationModelType, tinyint
from velocloud.models.configuration_module import ConfigurationModule
from velocloud.models.edge_object import EdgeObject
from velocloud.models.configuration_enterprise import ConfigurationEnterprise


@dataclass
class EnterpriseProxyGetEnterpriseProxyOperatorProfilesResultItem:
    """Enteprrise Proxy Get Enterprise Proxy Operator Profiles Result Item"""
    created: datetime
    description: str
    effective: datetime
    id: int
    modified: datetime
    name: str
    version: str
    configurationType: configurationModelType = None
    edgeCount: int = None
    logicalId: str = None
    modules: List(ConfigurationModule) = field(default_factory=list)
    schemaVersion: str = None
    isStaging: tinyint = None
    edges: List(EdgeObject) = field(default_factory=list)
    enterprises: List(ConfigurationEnterprise) = field(default_factory=list)

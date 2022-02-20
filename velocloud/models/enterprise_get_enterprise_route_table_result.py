from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from velocloud.models.enums import configurationModelType, tinyint
from velocloud.models.configuration_module import ConfigurationModule
from velocloud.models.enterprise_route_collection import EnterpriseRouteCollection
from velocloud.models.exit_entity_type import ExitEntityType


@dataclass
class Exits:
    """Exits
    This is a custom class.
    """
    edges: List(ExitEntityType)
    hubs: List(ExitEntityType)
    gateways: List(ExitEntityType)
    nvs: List(ExitEntityType)


@dataclass
class Profile:
    """Profile
    This is a custom class.
    """
    id: int
    description: str
    name: str
    configurationType: configurationModelType = None
    created: datetime = None  # datetime
    edgeCount: int = None
    effective: datetime = None  # datetime
    logicalId: str = None
    modified: datetime = None  # datetime
    modules: List(ConfigurationModule) = field(default_factory=list)
    schemaVersion: str = None
    version: str = None
    isStaging: tinyint = None


@dataclass
class EnterpriseGetEnterpriseRouteTableResult:
    """Enterprise Get Enterprise Route Table Result"""
    profiles: List(Profile) = field(default_factory=list)
    subnets: List(EnterpriseRouteCollection) = field(default_factory=list)
    exits: Exits = None

from dataclasses import dataclass, field
from typing import List
from velocloud.models.authentication_service_radius_attribute import AuthenticationServiceRadiusAttribute


@dataclass
class Secondary:
    """Secondary
    This is a custom class.
    """
    port: int = None


@dataclass
class Primary:
    """Primary
    This is a custom class.
    """
    server: str
    secret: str
    port: int
    accountingPort: int = None


@dataclass
class AuthenticationServiceData:
    """Authentication Service Data"""
    type: str  # pattern: Radius
    primary: Primary = None
    secondary: Secondary = None
    radiusAttributes: List(AuthenticationServiceRadiusAttribute) = field(default_factory=list)

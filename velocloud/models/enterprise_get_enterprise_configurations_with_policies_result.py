from dataclasses import dataclass
from velocloud.models.enums import configurationModelType, enterpriseConfigurationFirewallState


@dataclass
class Policy:
    """Policy
    This is a custom class.
    """
    bizPolicyEnabled: bool
    deviceSettingsEnabled: bool
    firewall: enterpriseConfigurationFirewallState


@dataclass
class EnterpriseGetEnterpriseConfigurationsWithPoliciesResult:
    """Enterprise Get Enterprise Configurations With Policies Result"""
    # api docs show this as a list
    configurationType: configurationModelType = None
    created: str = None  # datetime?
    description: str = None
    edgeCount: int = None
    effective: str = None  # datetime?
    id: int = None
    isStaging: int = None
    logicalId: str = None
    modified: str = None  # datetime?
    name: str = None
    policies: Policy = None
    schemaVersion: str = None
    version: str = None

from dataclasses import dataclass, field
from typing import List


@dataclass
class EnterpriseInsertEnterpriseDelegationParams:
    """Enterprise Insert Enterprise Delegation Params"""
    enableEnterpriseDelegationToOperator: bool = None
    enableEnterpriseDelegationToProxy: bool = None
    enableEnterpriseUserManagementDelegationToOperator: bool = None
    delegateEdgeImageManagementToEnterprise: bool = None
    enableExportRestriction: bool = None
    assignedOperatorProfileConfigurationIds: List(int) = field(default_factory=list)

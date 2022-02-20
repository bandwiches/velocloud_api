from dataclasses import dataclass, field
from typing import List
from velocloud.models.enterprise_alert_configuration import EnterpriseAlertConfiguration


@dataclass
class EnterpriseInsertOrUpdateEnterpriseAlertConfigurationsResult:
    """Enterprise Insert or Update Enterprise Alert Configurations Result"""
    enterpriseAlertConfigurations: List(EnterpriseAlertConfiguration) = field(default_factory=list)

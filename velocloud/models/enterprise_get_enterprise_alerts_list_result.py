from dataclasses import dataclass
from typing import List
from velocloud.models.enterprise_get_enterprise_alerts_result_item import EnterpriseGetEnterpriseAlertsResultItem
from velocloud.models.list_metadata import ListMetadata


@dataclass
class EnterpriseGetEnterpriseAlertsListResult:
    """Enterprise Get Enterprise Alerts List Result"""
    data: List(EnterpriseGetEnterpriseAlertsResultItem)
    metaData: ListMetadata

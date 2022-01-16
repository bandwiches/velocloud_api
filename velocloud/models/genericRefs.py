from dataclasses import dataclass
from velocloud.models.enterprise_service import EnterpriseService


@dataclass
class GenericRefs:
    """Generic Refs"""
    data: EnterpriseService = None

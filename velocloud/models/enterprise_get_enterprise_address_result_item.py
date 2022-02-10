from dataclasses import dataclass

from velocloud.models.enums import enterpriseAddressEntity


@dataclass
class EnterpriseGetEnterpriseAddressResultItem:
    """Enterprise Get Enterprise Address Result Item"""
    address: str = None
    entity: enterpriseAddressEntity = None

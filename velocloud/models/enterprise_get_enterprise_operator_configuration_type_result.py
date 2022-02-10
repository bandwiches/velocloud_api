from dataclasses import dataclass

from velocloud.models.enums import configurationModelType


@dataclass
class EnterpriseGetEnterpriseOperatorConfigurationTypeResult:
    """Enterprise Get Enterprise Operator Configuration Type Result"""
    configurationType: configurationModelType

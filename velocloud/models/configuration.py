from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List


"""Enums"""


class ConfigurationModuleType(Enum):
    ENTERPRISE = "ENTERPRISE"
    OPERATOR = "OPERATOR"
    GATEWAY = "GATEWAY"


class ConfigurationModuleName(Enum):
    imageUpdate = "imageUpdate"
    controlPlane = "controlPlane"
    managementPlane = "managementPlane"
    firewall = "firewall"
    QOS = "QOS"
    deviceSettings = "deviceSettings"
    WarningmetaData = "WarningmetaData"
    properties = "properties"
    analyticsSettings = "analyticsSettings"


class ConfigurationType(Enum):
    NETWORK_BASED = "NETWORK_BASED"
    SEGMENT_BASED = "SEGMENT_BASED"


"""Dataclasses"""


@dataclass
class ConfigurationModule:
    """ Configuration Module (v4.2.1) """
    name: ConfigurationModuleName
    created: datetime = None  # Datetime
    effective: datetime = None  # Datetime
    modified: datetime = None  # Datetime
    id: int = None
    type: ConfigurationModuleType = None
    description: str = None
    configurationId: int = None
    data: dict = None
    schemaVersion: str = None
    version: str = None
    metadata: dict = None
    refs: dict = None

    def __repr__(self):
        return str(type(self))

    @staticmethod
    def from_dict(cls, profile: dict):
        created = None
        effective = None
        modified = None

        # Datetimes
        try:
            created = datetime.strptime(profile.get('created'), "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            effective = datetime.strptime(profile.get('effective'), "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        try:
            modified = datetime.strptime(profile.get('modified'), "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass

        return ConfigurationModule(
            name=ConfigurationModuleName(profile.get('name')),
            config_module_id=profile.get('id'),
            type=ConfigurationModuleType(profile.get('type')),
            description=profile.get('description'),
            configurationId=profile.get('configurationId'),
            data=profile.get('data'),
            schemaVersion=profile.get('schemaVersion'),
            version=profile.get('version'),
            metadata=profile.get('metadata'),
            refs=profile.get('refs'),
            created=created,
            effective=effective,
            modified=modified
        )


@dataclass
class ModelConfiguration:
    configurationType: ConfigurationType = None
    created: datetime = None  # Datetime
    description: str = None
    edgeCount: int = None
    effective: datetime = None  # Datetime
    __id: int = None
    logicalId: str = None
    modified: datetime = None  # Datetime
    modules: List[ConfigurationModule] = field(default_factory=list)
    name: str = None
    schemaVersion: str = None
    version: str = None
    isStaging: int = None

    def __repr__(self):
        return str(type(self))

    @property
    def config_model_id(self):
        return self.__id

    @config_model_id.setter
    def config_model_id(self, value: int):
        self.__id = value

    @classmethod
    def from_dict(cls, profile: dict):
        """Factory Method"""
        INST = cls()
        INST.configurationType = ConfigurationType(profile.get('configurationType'))
        try:
            INST.created = datetime.strptime(profile.get('created'), "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        INST.description = profile.get('description')
        INST.edgeCount = profile.get('edgeCount')
        try:
            INST.effective = datetime.strptime(profile.get('effective'), "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        INST.config_model_id = profile.get('id')
        INST.logicalId = profile.get('logicalId')
        try:
            INST.modified = datetime.strptime(profile.get('modified'), "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        for m in profile["modules"]:
            INST.modules.append(ConfigurationModule.from_dict(m))
        INST.name = profile.get('name')
        INST.schemaVersion = profile.get('schemaVersion')
        INST.version = profile.get('version')
        INST.isStaging = profile.get('isStaging')

        return INST

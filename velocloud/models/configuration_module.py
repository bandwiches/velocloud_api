from dataclasses import dataclass
from datetime import datetime
from velocloud.models.enums import unitName, unitType


@dataclass
class ConfigurationModule:
    """Configuration Module"""
    name: unitName
    created: datetime = None  # datetime
    effective: datetime = None  # datetime
    modified: datetime = None  # datetime
    id: int = None
    type: unitType = None
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

        return cls(
            name=unitName(profile.get('name')),
            config_module_id=profile.get('id'),
            type=unitType(profile.get('type')),
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

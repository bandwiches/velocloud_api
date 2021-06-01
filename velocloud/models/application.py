from dataclasses import dataclass, field
from datetime import datetime
from typing import List


""" ENUMS """


""" DATACLASSES """


@dataclass
class ApplicationMetadataUploadDetails:
    size: int

    def __repr__(self):
        return str(type(self))


@dataclass
class ApplicationMetadataManifest:
    description: str
    name: str
    version: str

    def __repr__(self):
        return str(type(self))


@dataclass
class ApplicationMetadata:
    blobId: int
    created: datetime
    description: str
    fileName: str
    _id: int
    logicalId: str
    manifest: ApplicationMetadataManifest
    modified: datetime
    name: str
    networkId: int
    type: str
    uploadDetails: ApplicationMetadataUploadDetails
    version: str

    def __repr__(self):
        return str(type(self))

    @property
    def app_metadata_id(self):
        return self._id


@dataclass
class IpPortMapping:
    subnets: List[str] = field(default_factory=list)
    tcpPorts: List[int] = field(default_factory=list)
    udpPorts: List[int] = field(default_factory=list)

    def __repr__(self):
        return str(type(self))


@dataclass
class ProtocolPortMapping:
    tcpPorts: List[int] = field(default_factory=list)
    udpPorts: List[int] = field(default_factory=list)

    def __repr__(self):
        return str(type(self))


@dataclass
class Application:
    _id: int
    _class: int
    description: str
    displayName: str
    knownIpPortMapping: IpPortMapping
    protocolPortMapping: ProtocolPortMapping
    name: str = None

    def __repr__(self):
        return str(type(self))

    @property
    def app_id(self):
        return self._id

    @property
    def app_class(self):
        return self._class

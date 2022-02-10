from dataclasses import dataclass
from velocloud.models.ip_port_mapping import IpPortMapping
from velocloud.models.protocol_port_mapping import ProtocolPortMapping


@dataclass
class Application:
    """Application"""
    _class: int  # Better way to do this?
    description: str
    displayName: str
    id: int
    knownIpPortMapping: IpPortMapping
    protocolPortMapping: ProtocolPortMapping
    name: str = None

    def __repr__(self):
        return str(type(self))

    @property
    def app_class(self):
        return self._class

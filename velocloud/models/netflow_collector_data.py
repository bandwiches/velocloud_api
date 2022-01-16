from dataclasses import dataclass


@dataclass
class NetflowCollectorData:
    """Netflow Collector Data"""
    name: str
    address: str
    port: int

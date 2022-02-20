from dataclasses import dataclass


@dataclass
class ExitEntityType:
    """Exit Entity Type"""
    id: int
    name: str
    logicalId: str
    type: str = None

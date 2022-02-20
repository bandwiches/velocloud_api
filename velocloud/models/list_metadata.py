from dataclasses import dataclass


@dataclass
class ListMetadata:
    """List Metadata"""
    limit: int
    more: bool
    nextPageLink: str = None
    prevPageLink: str = None

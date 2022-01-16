from dataclasses import dataclass


@dataclass
class ManagementPlaneProxy:
    """Management Plane Proxy
    This is a custom class.
    """
    primary: str
    secondary: str


@dataclass
class ManagementPlaneData:
    """Management Plane Data"""
    heartBeatSeconds: int
    managementPlaneProxy: ManagementPlaneProxy
    statsUploadSeconds: int
    timeSliceSeconds: int

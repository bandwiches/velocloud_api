from dataclasses import dataclass
from velocloud.models.enums import vnfVendor, vnfDownloadType, vnfDownloadStatus


@dataclass
class Service:
    """VNF Image Download Event Detail Service
    This is a custom class.
    """
    logicalId: str = None
    ref: str = None  # pattern: deviceSettings:securityVnf:service


@dataclass
class VnfImageDownloadEventDetail:
    """VNF Image Download Event Detail"""
    logicalId: str = None
    vnfType: str = None  # pattern: vnfImage
    vendor: vnfVendor = None
    downloadType: vnfDownloadType = None
    edgeSerialNumber: str = None
    isEdgeActive: bool = None
    status: vnfDownloadStatus = None
    description: str = None
    service: Service = None

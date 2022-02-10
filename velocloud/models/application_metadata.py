from dataclasses import dataclass
from datetime import datetime
from velocloud.models.application_metadata_manifest import ApplicationMetadataManifest
from velocloud.models.application_metadata_upload_details import ApplicationMetadataUploadDetails


@dataclass
class ApplicationMetadata:
    """Application Metadata"""
    blobId: int
    created: datetime  # datetime
    description: str
    fileName: str
    id: int
    logicalId: str
    manifest: ApplicationMetadataManifest
    modified: datetime  # datetime
    name: str
    networkId: int
    type: str
    uploadDetails: ApplicationMetadataUploadDetails
    version: str

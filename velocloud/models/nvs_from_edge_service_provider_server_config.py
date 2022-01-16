from dataclasses import dataclass
from velocloud.models.enums import nvsIkePropAuthenticationAlgorithm, nvsIkePropEncryptionAlgorithm, nvsIkePropPeerIkeId, nvsIpsecPropEncryptionAlgorithm, nvsIpsecPropTunnelType, nvsIpsecProtocol


# IPSec Proposal

@dataclass
class IpsecProp:
    """IPSec Proposal
    This is a custom class.
    """
    authenticationAlgorithm: str = None
    encryptionAlgorithm: nvsIpsecPropEncryptionAlgorithm = None
    ipsecTunnelType: nvsIpsecPropTunnelType = None
    lifeTimeSeconds: int = None
    reKeyTimer: int = None
    protocol: nvsIpsecProtocol = None
    dpdTimeoutSeconds: int = None
    dpdType: str = None


# Ike Proposal

@dataclass
class PeerIkeId:
    """Peer Ike ID
    This is a custom class.
    """
    ikeId: str = None
    ikeIdType: nvsIkePropPeerIkeId = None


@dataclass
class IkeProp:
    """IKE Proposal
    This is a custom class.
    """
    DHGroup: int = None
    PFS: int = None
    authenticationAlgorithm: nvsIkePropAuthenticationAlgorithm = None
    authenticationMethod: str = None
    dpdTimeoutSeconds: int = None
    encryptionAlgorithm: nvsIkePropEncryptionAlgorithm = None
    ikev1MainMode: bool = None
    lifeTimeSeconds: int = None
    peerIkeId: PeerIkeId = None
    protocolVersion: int = None


@dataclass
class NvsFromEdgeServiceProviderServerConfig:
    """NVS From Edge Service Provider Server Config"""
    IKEPROP: IkeProp = None
    IPSECPROP: IpsecProp = None
    localLinkIp: str = None
    nvsPublicIp: str = None
    peerLinkIp: str = None

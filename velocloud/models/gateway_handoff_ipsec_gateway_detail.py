from dataclasses import dataclass


@dataclass
class GatewayHandoffIpsecGatewayDetail:
    """Gateway Handoff IPSec Gateway Detail"""
    ipsecGatewayAddress: str
    strictHostCheck: bool = None
    strictHostCheckDN: str = None

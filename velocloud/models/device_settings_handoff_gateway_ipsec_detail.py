from dataclasses import dataclass


@dataclass
class DeviceSettingsHandoffGatewayIpsecDetail:
    """Device Settings - Handoff Gateway - IPSec Detail"""
    ipsecGatewayAddress: str = None
    strictHostCheck: bool = None

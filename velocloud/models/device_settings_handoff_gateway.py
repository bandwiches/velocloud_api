from dataclasses import dataclass

from velocloud.models.device_settings_handoff_gateway_ipsec_detail import DeviceSettingsHandoffGatewayIpsecDetail


@dataclass
class DeviceSettingsHandoffGateway:
    """Device Settings - Handoff Gateway"""
    logicalId: str = None
    ipsecDetail: DeviceSettingsHandoffGatewayIpsecDetail = None

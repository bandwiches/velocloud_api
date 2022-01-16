from dataclasses import dataclass
from velocloud.models.device_settings_multicast_pim_on_wan_overlay import DeviceSettingsMulticastPimOnWanOverlay
from velocloud.models.device_settings_multicast_rp import DeviceSettingsMulticastRp


@dataclass
class DeviceSettingsMulticast:
    """Device Settings - Multicast"""
    enabled: bool = None
    override: bool = None
    igmpHostQueryIntervalSeconds: int = None
    igmpMaxQueryResponse: int = None
    pimKeepAliveTimerSeconds: int = None
    pimOnWanOverlay: DeviceSettingsMulticastPimOnWanOverlay = None
    pimPruneIntervalSeconds: int = None
    rp: DeviceSettingsMulticastRp = None

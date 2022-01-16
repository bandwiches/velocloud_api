from dataclasses import dataclass, field
from typing import List
from velocloud.models.configuration_module_segment_metadata import ConfigurationModuleSegmentMetadata
from velocloud.models.device_settings_authentication import DeviceSettingsAuthentication
from velocloud.models.device_settings_bgp import DeviceSettingsBgp
from velocloud.models.device_settings_cloud_security import DeviceSettingsCloudSecurity
from velocloud.models.device_settings_dns import DeviceSettingsDns
from velocloud.models.device_settings_handoff_gateways import DeviceSettingsHandoffGateways
from velocloud.models.device_settings_icmp_probe import DeviceSettingsIcmpProbe
from velocloud.models.device_settings_icmp_responder import DeviceSettingsIcmpResponder
from velocloud.models.device_settings_multicast import DeviceSettingsMulticast
from velocloud.models.device_settings_nat import DeviceSettingsNat
from velocloud.models.device_settings_netflow import DeviceSettingsNetflow
from velocloud.models.device_settings_nvs_from_edge import DeviceSettingsNvsFromEdge
from velocloud.models.device_settings_multi_source_qos import DeviceSettingsMultiSourceQos
from velocloud.models.device_settings_ntp import DeviceSettingsNtp
from velocloud.models.device_settings_ospf import DeviceSettingsOspf
from velocloud.models.device_settings_snmp import DeviceSettingsSnmp
from velocloud.models.device_settings_static_route import DeviceSettingsStaticRoute
from velocloud.models.device_settings_syslog import DeviceSettingsSyslog
from velocloud.models.device_settings_vpn import DeviceSettingsVpn
from velocloud.models.device_settings_vqm import DeviceSettingsVqm
from velocloud.models.device_settings_vrrp import DeviceSettingsVrrp


@dataclass
class Route:
    """Route
    This is a custom class.
    """
    icmpProbes: List(DeviceSettingsIcmpProbe) = field(default_factory=list)
    icmpResponders: List(DeviceSettingsIcmpResponder) = field(default_factory=list)
    static: List(DeviceSettingsStaticRoute) = field(default_factory=list)


@dataclass
class DeviceSettingsSegment:
    """Device Settings - Segment"""
    authentication: DeviceSettingsAuthentication = None
    bgp: DeviceSettingsBgp = None
    css: DeviceSettingsCloudSecurity = None
    edgeDirect: DeviceSettingsNvsFromEdge = None
    dns: DeviceSettingsDns = None
    handOffControllers: DeviceSettingsHandoffGateways = None
    handOffGateways: DeviceSettingsHandoffGateways = None
    multiSourceQos: DeviceSettingsMultiSourceQos = None
    multicast: DeviceSettingsMulticast = None
    nat: DeviceSettingsNat = None
    netflow: DeviceSettingsNetflow = None
    ntp: DeviceSettingsNtp = None
    ospf: DeviceSettingsOspf = None
    routes: Route = None
    segment: ConfigurationModuleSegmentMetadata = None
    snmp: DeviceSettingsSnmp = None
    syslog: DeviceSettingsSyslog = None
    vpn: DeviceSettingsVpn = None
    vqm: DeviceSettingsVqm = None
    vrrp: DeviceSettingsVrrp = None

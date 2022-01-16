from dataclasses import dataclass, field
from typing import List
from velocloud.models.device_settings_bfd import DeviceSettingsBfd
from velocloud.models.device_settings_ha import DeviceSettingsHa
from velocloud.models.device_settings_l2_settings import DeviceSettingsL2Settings
from velocloud.models.device_settings_lan import DeviceSettingsLan
from velocloud.models.device_settings_model import DeviceSettingsModel
from velocloud.models.device_settings_multi_source_qos import DeviceSettingsMultiSourceQos
from velocloud.models.device_settings_ntp import DeviceSettingsNtp
from velocloud.models.device_settings_ntp_as_server import DeviceSettingsNtpAsServer
from velocloud.models.device_settings_radio_settings import DeviceSettingsRadioSettings
from velocloud.models.device_settings_routed_interface import DeviceSettingsRoutedInterface
from velocloud.models.device_settings_segment import DeviceSettingsSegment
from velocloud.models.device_settings_snmp import DeviceSettingsSnmp
from velocloud.models.device_settings_software_update import DeviceSettingsSoftwareUpdate
from velocloud.models.device_settings_tacacs import DeviceSettingsTacacs
from velocloud.models.device_settings_vnfs import DeviceSettingsVnfs


@dataclass
class Models:
    """Models
    This is a custom class.
    """
    data: DeviceSettingsModel = None


@dataclass
class SegmentBasedDeviceSettingsData:
    """Segment Based Device Settings Data"""
    bfd: DeviceSettingsBfd = None
    ha: DeviceSettingsHa = None
    lan: DeviceSettingsLan = None
    models: Models = None
    multiSourceQos: DeviceSettingsMultiSourceQos = None
    ntp: DeviceSettingsNtp = None
    ntpServer: DeviceSettingsNtpAsServer = None
    radioSettings: DeviceSettingsRadioSettings = None
    l2Settings: DeviceSettingsL2Settings = None
    routedInterfaces: List(DeviceSettingsRoutedInterface) = field(default_factory=list)
    segments: List(DeviceSettingsSegment) = field(default_factory=list)
    snmp: DeviceSettingsSnmp = None
    softwareUpdate: DeviceSettingsSoftwareUpdate = None
    tacacs: DeviceSettingsTacacs = None
    vnfs: DeviceSettingsVnfs = None

from dataclasses import dataclass, field
from typing import List

from velocloud.models.device_settings_radio import DeviceSettingsRadio


@dataclass
class DeviceSettingsRadioSettings:
    """Device Settings Radio Settings"""
    country: str = None
    radios: List(DeviceSettingsRadio) = field(default_factory=list)

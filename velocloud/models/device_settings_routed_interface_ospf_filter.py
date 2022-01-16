from dataclasses import dataclass, field
from typing import List
from ipaddress import IPv4Address
from velocloud.models.enums import routedInterfaceOspfFilterAction


@dataclass
class Filter:
    """Filter
    This is a custom class.
    """
    cidrIp: IPv4Address = None
    cidrPrefix: str = None
    action: routedInterfaceOspfFilterAction = None


@dataclass
class DeviceSettingsRoutedInterfaceOspfFilter:
    """Device Settings Routed Interface OSPF Filter"""
    defaultAction: routedInterfaceOspfFilterAction = None
    filters: List(Filter) = field(default_factory=list)

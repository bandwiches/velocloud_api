from dataclasses import dataclass, field
from typing import List
from ipaddress import IPv4Address
from velocloud.models.firewall_inbound_rule import FirewallInboundRule
from velocloud.models.firewall_segment import FirewallSegment


# Services Section

@dataclass
class Service_SSH:
    """Service - SSH
    This is a custom class.

    Args:
        allowSelectedIp ([IPv4Address]): List of IP addresses allowed SSH access
    """
    enabled: bool
    allowSelectedIp: List(IPv4Address) = field(default_factory=list)
    ruleLogicalId: str = None


@dataclass
class Service_LocalUI:
    """Service - Local UI
    This is a custom class.

    Args:
        allowSelectedIp ([IPv4Address]): List of IP addresses allowed UI access
    """
    enabled: bool
    portNumber: int
    allowSelectedIp: List(IPv4Address) = field(default_factory=list)
    ruleLogicalId: str = None


@dataclass
class Service_Console:
    """Service - Console
    This is a custom class.
    """
    enabled: bool


@dataclass
class Service_SNMP:
    """Service - SNMP
    This is a custom class.

    Args:
        allowSelectedIp ([IPv4Address]): List of IP addresses allowed SNMP access
    """
    enabled: bool
    allowSelectedIp: List(IPv4Address) = field(default_factory=list)
    ruleLogicalId: str = None


@dataclass
class Service_ICMP:
    """Service - ICMP
    This is a custom class.

    Args:
        allowSelectedIp ([IPv4Address]): List of IP addresses allowed ICMP access
    """
    enabled: bool
    allowSelectedIp: List(IPv4Address) = field(default_factory=list)
    ruleLogicalId: str = None


@dataclass
class Services:
    """Services
    This is a custom class.
    """
    loggingEnabled: bool
    ssh: Service_SSH = None
    localUi: Service_LocalUI = None
    console: Service_Console = None
    snmp: Service_SNMP = None
    icmp: Service_ICMP = None


# Network Protection Settings Section

@dataclass
class IpBasedAttacks:
    """IP Based Attacks
    This is a custom class.
    """
    enableUnknownProtocol: bool = None
    enableInsecureOptions: bool = None


@dataclass
class IcmpBasedAttacks:
    """ICMP Based Attacks
    This is a custom class.
    """
    enablePingOfDeath: bool = None
    enableFragment: bool = None


@dataclass
class TcpBasedAttacks:
    """TCP Based Attacks
    This is a custom class.
    """
    invalidFlags: bool = None
    enableLand: bool = None
    enableSynFragment: bool = None


@dataclass
class NetworkProtectionSettings:
    """Network Protection Settings
    This is a custom class.
    """
    denylistDuration: int = None
    newConnectionThreshold: int = None
    denylist: bool = None
    detectionTime: int = None
    tcpBasedAttacksEnabled: bool = None
    tcpBasedAttacks: TcpBasedAttacks = None
    icmpBasedAttacksEnabled: bool = None
    icmpBasedAttacks: IcmpBasedAttacks = None
    ipBasedAttacksEnabled: bool = None
    ipBasedAttacks: IpBasedAttacks = None


# Statefule Firewall Settings Section

@dataclass
class StatefulFirewallSettings:
    """Statefule Firewall Settings
    This is a custom class.
    """
    establishedTcpFlowTimeout: int = None
    nonEstablishedTcpFlowTimeout: int = None
    udpFlowTimeout: int = None
    otherFlowTimeout: int = None


@dataclass
class FirewallData:
    """Firewall Data"""
    firewall_enabled: bool
    inbound: List(FirewallInboundRule)
    segments: List(FirewallSegment)
    stateful_firewall_enabled: bool = None
    firewall_logging_enabled: bool = None
    syslog_forwarding: bool = None
    statefulFirewallSettings: StatefulFirewallSettings = None
    networkProtectionSettings: NetworkProtectionSettings = None
    services: Services = None
    inboundLoggingEnabled: bool = False  # API has default value

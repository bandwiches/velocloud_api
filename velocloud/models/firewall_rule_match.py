from dataclasses import dataclass
from ipaddress import IPv4Address
from velocloud.models.enums import firewallRuleType


@dataclass
class FirewallRuleMatch:
    """Firewall Rule Match

    Args:
        appid (int): Integer ID corresponding to an application in the network-level application map
        classid (int): Integer ID corresponding to an application class in the network-level application map
        dscp (int): Integer ID indicating DSCP classification, where mappings are as follows:
            [EF:46,VA:44,AF11:10,AF12:12,AF13:14,AF21:18,AF22:20,AF23:22,AF31:26,AF32:28,AF33:30,AF41:34,AF42:36,AF43:38,CS0:0,CS1:8,CS2:16,CS3:24,CS4:32,CS5:40,CS6:48,CS7:56]
        sip (str): Source IP address
        sport_high (int): Upper bound of a source port range
        sport_low (int): Lower bound of a source port range
        sAddressGroup (str): Source address group reference
        sPortGroup (str): Source port group reference
        ssm (IPv4Address): Source subnet mask, e.g. 255.255.255.0
        smac (str): Source MAC address
        svlan (int): Integer ID for the source VLAN
        sInterface (str):
        os_version (int): Index corresponding to the OS in the array: [OTHER,WINDOWS,LINUX,MACOS,IOS,ANDROID,EDGE]
        hostname (str):
        dip (IPv4Address): Destination IP address
        dport_low (int): Lower bound of a destination port range
        dport_high (int): Upper bound of a destination port range
        dAddressGroup (str): Destination address group reference
        dPortGroup (str): Destination port group reference
        dsm (IPv4Address): Destination subnet mask e.g. 255.255.255.0
        dmac (str): Destination MAC address
        dvlan (int): Integer ID for the destination VLAN
        dInterface (str):
        proto (int): Integer ID corresponding to a protocol
        s_rule_type (firewallRuleType): Source rule type
        d_rule_type (firewallRuleType): Destination rule type
    """
    appid: int = None
    classid: int = None
    dscp: int = None
    sip: str = None
    sport_high: int = None
    sport_low: int = None
    sAddressGroup: str = None
    sPortGroup: str = None
    ssm: IPv4Address = None
    smac: str = None
    svlan: int = None
    sInterface: str = None
    os_version: int = None
    hostname: str = None
    dip: IPv4Address = None
    dport_low: int = None
    dport_high: int = None
    dAddressGroup: str = None
    dPortGroup: str = None
    dsm: IPv4Address = None
    dmac: str = None
    dvlan: int = None
    dInterface: str = None
    proto: int = None
    s_rule_type: firewallRuleType = None
    d_rule_type: firewallRuleType = None

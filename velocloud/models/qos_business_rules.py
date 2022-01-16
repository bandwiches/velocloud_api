from dataclasses import dataclass
from ipaddress import IPv4Address
from velocloud.models.enums import ruleType
from velocloud.models.route_action_object import RouteActionObject


@dataclass
class Action:
    """QoS Business Rules Action
    This is a custom class.
    """
    routeType: str = None
    allowConditionalBh: bool = None
    userDisableConditionalBh: bool = None
    edge2EdgeRouteAction: RouteActionObject = None
    edge2DataCenterRouteAction: RouteActionObject = None
    edge2CloudRouteAction: RouteActionObject = None
    QoS: dict = None
    sla: dict = None


@dataclass
class Match:
    """QoS Business Rules Match
    This is a custom  class.

    Args:
        appid (int):
        classid (int):
        dscp (int): Integer ID indicating DSCP classification, where mappings are as follows:
            [EF:46,VA:44,AF11:10,AF12:12,AF13:14,AF21:18,AF22:20,AF23:22,AF31:26,AF32:28,AF33:30,AF41:34,AF42:36,AF43:38,CS0:0,CS1:8,CS2:16,CS3:24,CS4:32,CS5:40,CS6:48,CS7:56]
        sip (IPv4Address):
        sport_high (int):
        sport_low (int):
        sAddressGroup (str): Source address group reference
        sPortGroup (str): Source port group reference
        ssm (str):
        svlan (int):
        sInterface (str):
        os_version (int): Index corresponding to the OS in the array: [OTHER,WINDOWS,LINUX,MACOS,IOS,ANDROID,EDGE]
        hostname (str):
        dip (str):
        dport_low (int):
        dport_high (int):
        dAddressGroup (str): Destination address group reference
        dPortGroup (str): Destination port group reference
        dsm (str):
        dvlan (int):
        proto (int):
        s_rule_type (str):
        d_rule_type (str):

    """
    appid: int = None
    classid: int = None
    dscp: int = None
    sip: IPv4Address = None
    sport_high: int = None
    sport_low: int = None
    sAddressGroup: str = None
    sPortGroup: str = None
    ssm: str = None
    svlan: int = None
    sInterface: str = None
    os_version: int = None
    hostname: str = None
    dip: IPv4Address = None
    dport_low: int = None
    dport_high: int = None
    dAddressGroup: str = None
    dPortGroup: str = None
    dsm: str = None
    dvlan: int = None
    proto: int = None
    s_rule_type: ruleType = None
    d_rule_type: ruleType = None


@dataclass
class QosBusinessRules:
    """QoS Business Rules

    Args:
        name (str):
        match (Match):
        action (Action):
        ruleLogicalId (str): Globally unique identifier for the policy rule
    """
    name: str = None
    match: Match = None
    action: Action = None
    ruleLogicalId: str = None

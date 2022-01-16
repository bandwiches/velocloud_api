from dataclasses import dataclass


@dataclass
class RouteActionObject:
    """Route Action Object"""
    interface: str = None
    linkInternalLogicalId: str = None
    linkPolicy: str = None
    routeCfg: dict = None
    routePolicy: str = None
    serviceGroup: str = None
    vlanId: int = None
    wanlink: str = None
    linkCosLogicalId: str = None
    linkOuterDscpTag: str = None
    linkInnerDscpTag: str = None

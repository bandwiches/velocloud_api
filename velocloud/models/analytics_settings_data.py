from dataclasses import dataclass


@dataclass
class ConfigEndpoint:
    """Config Endpoint
    This is a custom class.
    """
    host: str
    cert: str


@dataclass
class AnalyticsEndpoint:
    """Analytics Endpoint
    This is a custom class.
    """
    host: str = None
    cert: str = None
    isDynamicIP: bool = None


@dataclass
class AnalyticsSettingsData:
    """Analytics Settings Data"""
    mode: str = None
    enterpriseObjectId: str = None
    analyticsEndpoint: AnalyticsEndpoint = None
    configEndpoint: ConfigEndpoint = None

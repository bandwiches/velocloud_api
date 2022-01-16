from dataclasses import dataclass


@dataclass
class ImageUpdateScheduledTime:
    """Image Update Scheduled Time"""
    dayOfWeek: int
    specified: bool
    timeOfDayMins: int
    useEdgeTimeZone: bool

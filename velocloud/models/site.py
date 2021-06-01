from dataclasses import dataclass
from datetime import datetime


@dataclass
class Site:
    """ Edge Site (v4.2.1) """
    id: int = None
    created: datetime = None  # Datetime
    name: str = None
    logicalId: str = None
    contactName: str = None
    contactPhone: str = None
    contactMobile: str = None
    contactEmail: str = None
    streetAddress: str = None
    streetAddress2: str = None
    city: str = None
    state: str = None
    postalCode: str = None
    country: str = None
    lat: float = None
    lon: float = None
    timezone: str = None
    locale: str = None
    shippingSameAsLocation: int = None
    shippingContactName: str = None
    shippingAddress: str = None
    shippingAddress2: str = None
    shippingCity: str = None
    shippingState: str = None
    shippingCountry: str = None
    shippingPostalCode: str = None
    modified: datetime = None  # Datetime

    def __repr__(self):
        return str(type(self))

    @classmethod
    def from_dict(cls, profile: dict):
        """Site Factory"""
        inst = cls()
        inst.id = profile.get("id")
        try:
            inst.created = datetime.strptime(profile["created"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        inst.name = profile.get("name")
        inst.logicalId = profile.get("logicalId")
        inst.contactName = profile.get("contactName")
        inst.contactPhone = profile.get("contactPhone")
        inst.contactMobile = profile.get("contactMobile")
        inst.contactEmail = profile.get("contactEmail")
        inst.streetAddress = profile.get("streetAddress")
        inst.streetAddress2 = profile.get("streetAddress2")
        inst.city = profile.get("city")
        inst.state = profile.get("state")
        inst.postalCode = profile.get("postalCode")
        inst.country = profile.get("country")
        inst.lat = profile.get("lat")
        inst.lon = profile.get("long")
        inst.timezone = profile.get("timezone")
        inst.locale = profile.get("locale")
        inst.shippingSameAsLocation = profile.get("shippingSameAsLocation")
        inst.shippingContactName = profile.get("shippingContactName")
        inst.shippingAddress = profile.get("shippingAddress")
        inst.shippingAddress2 = profile.get("shippingAddress2")
        inst.shippingCity = profile.get("shippingCity")
        inst.shippingState = profile.get("shippingState")
        inst.shippingCountry = profile.get("shippingCountry")
        inst.shippingPostalCode = profile.get("shippingPostalCode")
        try:
            inst.modified = datetime.strptime(profile["modified"], "%Y-%m-%dT%H:%M:%S.%fZ")
        except ValueError:
            pass
        return inst

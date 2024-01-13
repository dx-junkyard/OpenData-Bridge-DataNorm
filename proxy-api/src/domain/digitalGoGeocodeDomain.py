from dataclasses import dataclass

@dataclass
class DigitalGoGeocodeDomain:
    lg_code: str
    town_id: str
    fulladdress: str
    prefecture: str
    city: str
    town: str
    lat: float
    lon: float

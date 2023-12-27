from dataclasses import dataclass

@dataclass
class GeocodeDomain:
    code: str
    aza_id: str
    prefectures: str
    municipalities: str
    aza: str
    latitude: str
    longitude: str

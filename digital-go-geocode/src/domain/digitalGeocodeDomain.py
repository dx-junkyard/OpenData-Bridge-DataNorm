from dataclasses import dataclass

@dataclass
class DigitalGeocodeDomain:
    output: str
    prefecture: str
    match_level: int
    city: str
    town: str
    town_id: str
    lg_code: str
    other: str
    lat: float
    lon: float
    block: str
    block_id: str
    addr1: str
    addr1_id: str
    addr2: str
    addr2_id: str

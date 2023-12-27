import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_secret
from domain.geocodeDomain import GeocodeDomain
from repository.geocodeRepository import GeocodeRepository

class GeocodeService(object):
    def __init__(self):
        self.repository = GeocodeRepository()

    def get(self, city_block_id: int, residence_id: int, address: str) -> GeocodeDomain:
        return GeocodeRepository.get(city_block_id, residence_id, address)

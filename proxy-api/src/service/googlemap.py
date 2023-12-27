import googlemaps

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_secret

class GeocodeService(object):
    def __init__(self):
        SECRET_NAME = "GoogleMapsAPIKey"
        self._API_KEY = get_secret(SECRET_NAME) # APIキーのシークレット名を指定

    def get(self, address):
        gmaps = googlemaps.Client(key=self._API_KEY)
        geocode_result = gmaps.geocode(address)

        return geocode_result



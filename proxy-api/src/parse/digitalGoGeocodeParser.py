import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.digitalGoGeocodeDomain import DigitalGoGeocodeDomain

import json

class DigitalGoGeocdeParser:
    def parse(self, jsonStr: str) -> DigitalGoGeocodeDomain:
        data = json.loads(jsonStr)

        digitalGeocodeData = {
            "lg_code": data.get("lg_code", ""),
            "town_id": data.get("town_id", ""),
            "fulladdress": data.get("output", ""),
            "prefecture": data.get("prefecture", ""),
            "city": data.get("city", ""),
            "town": data.get("town", ""),
            "lat": data.get("lat", 0),
            "lon": data.get("lon", 0)            
        }

        return DigitalGoGeocodeDomain(**digitalGeocodeData)


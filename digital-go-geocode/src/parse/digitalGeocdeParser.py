import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from domain.digitalGeocodeDomain import DigitalGeocodeDomain

import json

class DigitalGeocdeParser:
    def parse(self, jsonStr: str) -> DigitalGeocodeDomain:
        data = json.loads(jsonStr)[0]

        digitalGeocodeData = {
            "output": data["result"].get("output", "") if "result" in data else "",
            "prefecture": data["result"].get("prefecture", "") if "result" in data else "",
            "match_level": data["result"].get("match_level", 0) if "result" in data else 0,
            "city": data["result"].get("city", "") if "result" in data else "",
            "town": data["result"].get("town", "") if "result" in data else "",
            "town_id": data["result"].get("town_id", "") if "result" in data else "",
            "lg_code": data["result"].get("lg_code", "") if "result" in data else "",
            "other": data["result"].get("other", "") if "result" in data else "",
            "lat": data["result"].get("lat", 0) if "result" in data else 0,
            "lon": data["result"].get("lon", 0) if "result" in data else 0,
            "block": data["result"].get("block", "") if "result" in data else "",
            "block_id": data["result"].get("block_id", "") if "result" in data else "",
            "addr1": data["result"].get("addr1", "") if "result" in data else "",
            "addr1_id": data["result"].get("addr1_id", "") if "result" in data else "",
            "addr2": data["result"].get("addr2", "") if "result" in data else "",
            "addr2_id": data["result"].get("addr2_id", "") if "result" in data else ""
        }

        return DigitalGeocodeDomain(**digitalGeocodeData)


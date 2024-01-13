import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import logging
import requests

from parse.digitalGoGeocodeParser import DigitalGoGeocdeParser
from domain.digitalGoGeocodeDomain import DigitalGoGeocodeDomain
from utils import get_secret

class DigitalGoGeocodeService(object):
    def __init__(self):
        self.parser = DigitalGoGeocdeParser()
        SECRET_NAME = "digital-go-geocode-url"
        self._ENDPOINT = get_secret(SECRET_NAME)

    def get(self, address: str) -> DigitalGoGeocodeDomain:
        path = '/digital_geocode'
        params = f'?address={address}'  # 日本語から英語への翻訳
        constructed_url = self._ENDPOINT + path + params
        response = requests.get(constructed_url)
        logging.info(response)
        
        return self.parser.parse(response.text)

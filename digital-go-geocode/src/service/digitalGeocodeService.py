import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import logging
import subprocess

from parse.digitalGeocdeParser import DigitalGeocdeParser
from domain.digitalGeocodeDomain import DigitalGeocodeDomain

class DigitalGeocodeService(object):
    def __init__(self):
        self.parser = DigitalGeocdeParser()

    def get(self, address: str) -> DigitalGeocodeDomain:
        # コマンドを一つの文字列として定義
        cmd = f'echo "{address}" | abrg -'
        
        # シェルを介してコマンドを実行
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        return self.parser.parse(result.stdout)
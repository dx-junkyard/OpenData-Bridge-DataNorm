import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd

from domain.geocodeDomain import GeocodeDomain

class GeocodeRepository(object):
    def __init__(self):
        self.df = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resources', 'geocode', 'merged_jyuukyo.csv'))

    def get(self, city_block_id: int, residence_id: int, address: str) -> GeocodeDomain:
        _df = self.df[(self.df['街区id'] == city_block_id) & (self.df['住居id'] == residence_id) & (self.df['位置参照情報_大字・町丁目名'] == address)]

        if len(_df) == 0:
            return GeocodeDomain(
                code=-1,
                aza_id=-1,
                prefectures="",
                municipalities="",
                aza="",
                latitude=0.0,
                longitude=0.0
            )

        return GeocodeDomain(
            code=_df['全国地方公共団体コード'].values.tolist()[0],
            aza_id=_df['町字id'].values.tolist()[0],
            prefectures=_df['位置参照情報_都道府県名'].values.tolist()[0],
            municipalities=_df['位置参照情報_市区町村名'].values.tolist()[0],
            aza=_df['位置参照情報_大字・町丁目名'].values.tolist()[0],
            latitude=_df['代表点_緯度'].values.tolist()[0],
            longitude=_df['代表点_経度'].values.tolist()[0],
        )





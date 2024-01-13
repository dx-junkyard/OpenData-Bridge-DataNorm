import azure.functions as func
import logging
import json
from dataclasses import asdict

app = func.FunctionApp()

# from service.googlemap import GeocodeService
from src.service.geocodeService import GeocodeRepository

@app.route(route="geocode", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def geocode(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function for geocoding executed.')

    geocodeService = GeocodeRepository()

    city_block_id = int(req.params.get('city_block_id'))
    residence_id = int(req.params.get('residence_id'))
    address = req.params.get('address')

    if address:
        geocode_result = geocodeService.get(city_block_id, residence_id, address)
        return func.HttpResponse(
            json.dumps(asdict(geocode_result)),
            headers={"Content-Type": "application/json"}
        )
    else:
        return func.HttpResponse(
             "Please pass an address in the query string.",
             status_code=200
        )

from src.service.digitalGoGeocodeService import DigitalGoGeocodeService
@app.route(route="digital-go-geocode", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def digital_go_geocode(req: func.HttpRequest) -> func.HttpResponse:

    digitalGoGeocodeService = DigitalGoGeocodeService()

    address = req.params.get('address')

    if address:
        geocode_result = digitalGoGeocodeService.get(address)
        return func.HttpResponse(
            json.dumps(asdict(geocode_result)),
            headers={"Content-Type": "application/json"}
        )
    else:
        return func.HttpResponse(
             "Please pass an address in the query string.",
             status_code=200
        )

@app.route(route="hello", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def hello(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a hello request.')
    return func.HttpResponse("Hello World from /hello", status_code=200)

from src.service.translateService import TranslateService

@app.route(route="japanese-to-english", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def japanese_to_english(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function for jp2en executed.')
    translateService = TranslateService()

    jp_str = req.params.get('jp')

    en_str = translateService.jp2en(jp_str)

    return func.HttpResponse(
        json.dumps({"en" : en_str}),
        headers={"Content-Type": "application/json"}
    )


# 作業内容

# キーコンテナー
# デプロイ
# IAMで自分を追加()

# 関数アプリの設定のIDで状態をON（システム割り当てマネージドIDの有効化）
# キーコンテナーのIAMで設定した関数アプリにロールの割り当て（キーコンテナーシークレットユーザー)

# シークレットの追加



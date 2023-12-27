import azure.functions as func
import logging
import json
from dataclasses import asdict

app = func.FunctionApp()

# from service.googlemap import GeocodeService
from src.service.geocodeService import GeocodeRepository

@app.route(route="geocode", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def Geocode(req: func.HttpRequest) -> func.HttpResponse:
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

@app.route(route="hello", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def hello(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a hello request.')
    return func.HttpResponse("Hello World from /hello", status_code=200)

# 作業内容

# キーコンテナー
# デプロイ
# IAMで自分を追加()

# 関数アプリの設定のIDで状態をON（システム割り当てマネージドIDの有効化）
# キーコンテナーのIAMで設定した関数アプリにロールの割り当て（キーコンテナーシークレットユーザー)

# シークレットの追加



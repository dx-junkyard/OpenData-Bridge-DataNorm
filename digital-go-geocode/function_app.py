import logging
import json
from dataclasses import asdict

from flask import Flask, request, jsonify
from src.service.digitalGeocodeService import DigitalGeocodeService

app = Flask(__name__)

@app.route('/digital_geocode', methods=['GET'])
def geocode():
    geocodeService = DigitalGeocodeService()
    address = request.args.get('address')
    if address:
        geocode_result = geocodeService.get(address)
        return asdict(geocode_result)
    else:
        return "Please pass an address in the query string.", 200

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World from /hello", 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
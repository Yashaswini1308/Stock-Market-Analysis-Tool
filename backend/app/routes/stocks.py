from flask import Blueprint, jsonify, request
import os
import requests

stocks_bp = Blueprint('stocks', __name__, url_prefix='/stocks')

@stocks_bp.route('/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'

    response = requests.get(url)
    data = response.json()

    return jsonify(data)


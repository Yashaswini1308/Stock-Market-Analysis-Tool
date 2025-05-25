from flask import Blueprint, jsonify

stocks_bp = Blueprint('stocks', __name__, url_prefix='/stocks')

@stocks_bp.route('/', methods=['GET'])
def get_stocks():
    # Placeholder for now
    data = {
        "message": "This will return stock data"
    }
    return jsonify(data)

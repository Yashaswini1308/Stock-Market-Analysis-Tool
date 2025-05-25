from flask import Blueprint, jsonify

watchlist_bp = Blueprint('watchlist', __name__, url_prefix='/watchlist')

@watchlist_bp.route('/', methods=['GET'])
def get_watchlist():
    # Placeholder for now
    data = {
        "message": "This will return watchlist data"
    }
    return jsonify(data)

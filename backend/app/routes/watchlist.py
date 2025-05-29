from flask import Blueprint, jsonify, request
from app.models import Watchlist
from app import db

# Create Blueprint for watchlist routes
watchlist_bp = Blueprint('watchlist', __name__, url_prefix='/watchlist')

# GET all watchlist items
@watchlist_bp.route('/', methods=['GET'])
def get_watchlist():
    watchlist_items = Watchlist.query.all()
    return jsonify([item.to_dict() for item in watchlist_items]), 200

# POST add new symbol to watchlist
@watchlist_bp.route('/', methods=['POST'])
def add_to_watchlist():
    data = request.get_json()
    symbol = data.get('symbol')

    if not symbol:
        return jsonify({"error": "Symbol is required"}), 400

    new_item = Watchlist(symbol=symbol)
    db.session.add(new_item)
    db.session.commit()

    return jsonify(new_item.to_dict()), 201

# DELETE a watchlist item by ID
@watchlist_bp.route('/<int:item_id>', methods=['DELETE'])
def remove_from_watchlist(item_id):
    item = Watchlist.query.get(item_id)

    if not item:
        return jsonify({"error": "Item not found"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted"}), 200

# GET a single watchlist item by ID
@watchlist_bp.route('/<int:item_id>', methods=['GET'])
def get_watchlist_item(item_id):
    item = Watchlist.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    return jsonify(item.to_dict()), 200

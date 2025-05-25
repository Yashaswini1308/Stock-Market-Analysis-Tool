from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for frontend-backend communication

    from .routes.stocks import stocks_bp
    from .routes.watchlist import watchlist_bp

    app.register_blueprint(stocks_bp)
    app.register_blueprint(watchlist_bp)

    return app

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    load_dotenv()

    app = Flask(__name__)
    CORS(app) #Enable CORS foe frontend-backend communication

    # Load database URL from environment
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes.stocks import stocks_bp
    from .routes.watchlist import watchlist_bp

    app.register_blueprint(stocks_bp)
    app.register_blueprint(watchlist_bp)

    return app

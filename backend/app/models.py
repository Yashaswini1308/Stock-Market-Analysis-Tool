from app import db

class Watchlist(db.Model):
    __tablename__ = 'watchlist'  # this is important!

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "symbol": self.symbol
        }

from app import db

class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key = True)
    first = db.Column(db.String(30), nullable=False)
    last = db.Column(db.String(30), nullable=False)
    quote = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Name: {self.first} {self.last}. Quote: {self.quote}"
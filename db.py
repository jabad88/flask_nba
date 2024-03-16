from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.integer, primary_key = True)
    first = db.Column(db.string(30), nullable=False)
    last = db.Column(db.string(30), nullable=False)
    quote = db.Column(db.Text, nullable=False)
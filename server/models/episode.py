from server.app import db
from datetime import date

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=date.today)
    number = db.Column(db.Integer, nullable=False)

    appearances = db.relationship("Appearance", backref="episode", cascade="all, delete")

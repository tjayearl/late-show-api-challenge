from server.extensions import db

class Episode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)
    appearances = db.relationship("Appearance", backref="episode", cascade="all, delete")
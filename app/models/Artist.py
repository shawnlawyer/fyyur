from app import db
import datetime

class Artist(db.Model):
    __tablename__ = 'Artist'


    _default_fields = [
        "name",
    ]

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    genres = db.Column(db.ARRAY(db.String))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String)
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String)
    image_link = db.Column(db.String)

    def __repr__(self):
        return '<Artist %r>' % self.name

    @property
    def upcoming(self):
        print(self.shows)
        return self.shows

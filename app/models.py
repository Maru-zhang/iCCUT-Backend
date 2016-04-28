__author__ = 'Maru'

from app import db

class FreeVideo(db.Model):
    id = db.Column(db.String(255),primary_key=True)
    title = db.Column(db.String(255))
    url = db.Column(db.String(255))
    leve1 = db.Column(db.String(255))
    leve2 = db.Column(db.String(255))
    time = db.Column(db.DateTime)
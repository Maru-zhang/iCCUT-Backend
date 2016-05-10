__author__ = 'Maru'

from app import db


class FreeVideo(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    url = db.Column(db.String(255))
    leve1 = db.Column(db.String(255))
    leve2 = db.Column(db.String(255))

    def  __init__(self,title,url,leve1,leve2):
        self.title = title
        self.url = url
        self.leve1 = leve1
        self.leve2 = leve2

    def __repr__(self):
        return '<FreeVideo %r>' % self.title



class Comment(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(140))
    datetime = db.Column(db.DateTime)
    good = db.Column(db.Integer)


class History(db.Model):

    id = db.Column(db.Integer,primary_key=True)

    def __init__(self,user,video):
        self.user_id = user
        self.video_id = video



class News(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    url = db.Column(db.String(50))
    datetime = db.Column(db.String(30))

    def __init__(self,title,url,datetime):
        self.title = title
        self.url = url
        self.datetime = datetime

    def __repr__(self):
        return '<News %r>' % self.title



class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(20))

    def __init__(self, username, email,password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
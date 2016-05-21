__author__ = 'Maru'

from app import db

class Video(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    url = db.Column(db.String(255))
    leve1 = db.Column(db.String(255))
    leve2 = db.Column(db.String(255))
    cover = db.Column(db.String(255))
    comments = db.relationship('Comment',backref=db.backref('video'),lazy='dynamic')


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
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    video_id = db.Column(db.Integer,db.ForeignKey('video.id'))

    def __init__(self,content,datetime,good,user,video):
        self.content = content
        if datetime is None:
            self.datetime = datetime.utcnow()
        self.good = good
        self.user = user
        self.video = video

    def __repr__(self):
        return '<Comment %r>' % self.content

historys = db.Table('historys',
    db.Column('video_id',db.Integer,db.ForeignKey('video.id')),
    db.Column('history_id',db.Integer,db.ForeignKey('history.id'))
)

class History(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    videos = db.relationship('Video',secondary=historys,backref=db.backref('history', lazy='dynamic'))




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

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "datetime": self.datetime
        }



class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(20))
    comments = db.relationship('Comment',backref=db.backref('user'),lazy='dynamic')
    history = db.relationship('History',backref=db.backref('user'),uselist=False)


    def __init__(self, username, email,password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username
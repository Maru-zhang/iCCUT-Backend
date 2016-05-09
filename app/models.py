__author__ = 'Maru'

from app import db
from datetime import datetime

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
		self.leve2 = leve1

	def __repr__(self):
 		return '<FreeVideo %r>' % self.title

 Class Comment(db.Model):

 	id = db.Column(db.Integer,primary_key=True)
 	from_id = db.Column(db.Integer,db.ForeignKey(''user.id))
 	user = db.relationship('User',backref=db.backref('cmts',lazy='dynamic'))
 	to_id = db.Column(db.Integer,db.ForeignKey('video.id'))
 	video = db.relationship('FreeVideo',backref=db.backref('fds',lazy='dynamic'))
 	content = db.Column(db.String(140))
 	time = db.Column(db.DateTime)

 class New(db.Model):

 	id = db.Column(db.Integer,primary_key=True)
 	title = db.Column(db.String(50))
 	url = db.Column(db.String(50))

 	def __init__(self, arg):
 		super(New, self).__init__()
 		self.arg = arg
 		

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
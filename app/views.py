# -*- coding: UTF-8 -*-
__author__ = 'Maru'
from flask import  request,jsonify
from app import app,db
from app.models import Video,User,News,Comment
import json
import base64

# 200 == Success
# -1  == Error
# -2  == No more data
#

pageCount = 20
defCat = {
    "documentary": "",
    "study": "",
    "cartoon": "",
    "movie": ""
}

@app.route('/')
def index():
    return "Hello, this is iCCUT backend!"


@app.route('/api/login',methods=['POST'])
def login():
    try:
        email = request.args.get('email')
        password = request.args.get('password')
        user = User.query.filter_by(email=email).first()

        if user == None:
            return formattingData(code=-1,msg='Not exit such account!',data=[])

        if user.password == password:
            return formattingData(200,msg='Login success.',data={
                "id": user.id,
                "username": user.username,
                "email": user.email
            })
        else:
            return formattingData(code=-1,msg='Incorrect password.',data=[])



    except KeyError,e:
        return formattingData(code=-1,msg='Sorry,login failed.',data=[])

@app.route('/api/register',methods=['POST'])
def register():
    try:
        name = request.args.get('username')
        email = request.args.get('email')
        password = request.args.get('password')

        user = User.query.filter_by(email=email).first()

        if user != None:
            return formattingData(code=-1,msg='Sorry,this email already been registered!',data=[])

        user = User(username=name,email=email,password=password)
        db.session.add(user)
        db.session.commit()

        return formattingData(code=200,msg='Register success!',data={
            "id":user.id,
            "username": user.username,
            "email": user.username,
            "password": user.password
        })
    except KeyError,e:
        return formattingData(code=-1,msg='Sorry,register failed.',data=[])


@app.route('/api/newslist',methods=['POST'])
def newsList():

    try:
        index = request.args.get("index")

        if index == None:
            result = News.query.offset(int(pageCount)*int(index)).limit(pageCount).all()
            return formattingData(code=200,msg='Fetch success.',data=[new.serialize() for new in result])


        result = News.query.offset(int(pageCount)*int(index)).limit(pageCount).all()
        return formattingData(code=200,msg='Fetch success.',data=[new.serialize() for new in result])

    except KeyError,e:
        return formattingData(code=-1,msg='Sorry,fetch list Fail.')

@app.route('/api/vides',methods=['POST'])
def videoList():

    try:
        index = request.args.get("index")
        category = request.args.get("category")

        if index == None or category == None:
            return formattingData(code=-1,msg='Sorry,request paramaters are missing!')

        cateMap = defCat[category]
        result = Video.query.offset(int(pageCount)*int(index)).filter(Video.leve1 == cateMap).limit(pageCount).all()
        return formattingData(code=200,msg='Fetch videos success.',data=[video.serialize() for video in result])


    except KeyError,e:
        return formattingData(code=-1,msg='Sorry,fetch video list fail.',data=[])

@app.route('/api/commentlist',methods=['POST'])
def commentList():

    video_id = request.args.get("videoid")
    index    = request.args.get("index")

    if video_id == None or index == None:
        return formattingData(code=-1,msg='Sorry,args are missing.',data=[])

    try:
        video = Video.query.filter(Video.id == video_id).first()
        comments = video.comments.offset(int(pageCount)*int(index)).limit(pageCount).all()
        return formattingData(code=200,msg='Fetch comments success.',data=[com.serialize() for com in comments])
    except KeyError,e:
        return formattingData(code=-1,msg='Sorry,fetch list fail.')


@app.route('/api/add_comment',methods=['POST'])
def commitComment():

    content = request.args.get("content")
    user_id = request.args.get("uid")
    video_id = request.args.get("vid")

    if content == None or user_id == None or video_id == None:
        return formattingData(code=-1,msg='Args missing.',data=[])

    try:
        com = Comment(content=content,user_id=user_id,video_id=video_id)
        db.session.add(com)
        db.session.commit()
    except KeyError,e:
        return formattingData(code=-1,msg='Submit fail.',data=[])


@app.route('/api/historylist',methods=['POST'])
def historyList():

    uid = request.args.get("uid")
    index = request.args.get("index")

    if uid == None or index == None:
        return formattingData(code=-1,msg="Args missing.",data=[])

    try:

        user = User.query.filter_by(User.id == uid).first()
        list = user.history.offset(int(pageCount)*int(index)).limit(pageCount).all()
    except KeyError,e:
        return formattingData(code=-1,msg='Fetch hstorys fail.',data=[])

    pass

@app.route('/api/add_history',methods=['POST'])
def addHistory():
    pass


def formattingData(code,msg,data):
    return jsonify(
        {
            "code": code,
            "msg" : msg,
            "data": data
        }
    )

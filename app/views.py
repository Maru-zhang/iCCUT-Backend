# -*- coding: UTF-8 -*-
__author__ = 'Maru'
from flask import  render_template,request,redirect,url_for,session,jsonify
from app import app,db
from app.models import Video,User
import base64



@app.route('/index')
def index():
    return "Hello, this is iCCUT backend!"


@app.route('/api/login',methods=['POST','GET'])
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

@app.route('/api/register',methods=['POST','GET'])
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


@app.route('/test')
def test():

    print User.query.all()

    return 'sss'


def formattingData(code,msg,data):
    return jsonify(
        {
            "code": code,
            "msg": msg,
            "data": data
        }
    )
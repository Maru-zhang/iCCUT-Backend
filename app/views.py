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

    return "dsadas"

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
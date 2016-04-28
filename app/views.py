# -*- coding: UTF-8 -*-
__author__ = 'Maru'
from flask import  render_template,request,redirect,url_for,session
from app import app,db
from app.models import FreeVideo


@app.route('/index')
def index():
    return "Hello, this is iCCUT backend!"

@app.route('/test')
def test():
    aaa = FreeVideo.query.first()
    print aaa
    return "dsa"
# -*- coding: UTF-8 -*-
__author__ = 'Maru'
from flask import  render_template,request,redirect,url_for,session
from app import app,db
from app.models import Video


@app.route('/index')
def index():
    return "Hello, this is iCCUT backend!"

@app.route('/test')
def test():

    return "dsa"
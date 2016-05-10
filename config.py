__author__ = 'Maru'

import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

import os
from flask_sqlalchemy import SQLAlchemy

from application import app

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy(app)


def init_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.create_all()

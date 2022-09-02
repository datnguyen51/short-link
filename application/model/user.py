from application.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)
    date = db.Column(db.DateTime)
    email = db.Column(db.String)
    count = db.Column(db.Integer)
    type = db.Column(db.Integer)
    active = db.Column(db.Boolean, default=0)
    total_point = db.Column(db.Integer, default=0)
    # link = Set('Link')
    # comment = Set('Comment')
    # token = Set('Token')
    # rate = Set('Rate')
    # report = Set('Report')

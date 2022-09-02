import re
import hashlib
import datetime

from flask import Response, Flask
from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, get_jwt_identity)

from application.database import db
from application.model.user import User


class Registration(Resource):
    def post(self, request):
        data = request.json()
        name = data.get('name')
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        regex_username = r"^[A-Za-z\s].{4,20}$"
        regex_gmail = r"^(([^<>()\[\]\\.,;:\s@\"]+(\.[^<>()\[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
        regex_password = r"^(?=.*\d)(?=.*[a-z]).{8,20}$"

        if not (re.match(regex_username, data['username'], flags=0)):
            return {'Username': 'Tên không hợp lệ', 'status': 404}, 404
        if not (re.match(regex_password, data['password'], flags=0)):
            return {'Password': 'Mật khẩu không hợp lệ', 'status': 404}, 404
        if not (re.match(regex_gmail, data['email'], flags=0)):
            return {'Email': 'Email không hợp lệ', 'status': 404}, 404

        record_username = db.session.query(User).filter(username=username).exists()
        if record_username:
            return {'Username': 'Tai khoan da ton tai', 'status': 404}, 404

        record_email = db.session.query(User).filter(email=email).exists()
        if record_email:
            return {'Username': 'Tai khoan da ton tai', 'status': 404}, 404

        passwrd = hashlib.md5(password.encode('utf-8'))

        record_user = User()
        record_user.name = name
        record_user.username = username
        record_user.password = passwrd
        record_user.email = email

        db.session.add(record_user)
        db.session.commit()

        return {'message': 'Thành công',
                'status': 200,
                }, 200

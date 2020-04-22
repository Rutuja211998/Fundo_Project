"""
This file contains UserService class which contains register, login, activate, logout, forgot password and reset password functions.
Author: Rutuja Tikhile
Date:6/3/2020
"""
from response import Response
import jwt
import json
from model.db_query import Query
db_obj = Query()
from config.redis_connection import RedisCon
redis_obj = RedisCon()
from vendor.sendmail import SMTP_Mail
import cgi, os


class UserService:
    # Here data is inserted into the database.
    def registration(self, user_data, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong!",
                "data": []
            }
            read_data = db_obj.read(table_name="users", column_name="email", column_value=user_data['email'])
            if read_data == []:
                db_obj.insert(data=user_data, table_name='users')
                user_email = user_data['email']
                db_data = db_obj.read(table_name="users", column_name="email", column_value=user_data['email'])
                user_id = db_data[0][0]
                email = db_data[0][2]
                token = jwt.encode({'id': user_id}, 'secret', algorithm='HS256').decode('utf-8')
                print(token)
                host = that.headers['Host']
                protocol = that.protocol_version.split('/')[0].lower()
                message = f"Click on the link below to confirm your registration: {protocol}://{host}/activate/?token={token}"
                SMTP_Mail().do_mailing(token, email)
                response = {
                    "success": True,
                    "message": "User is Registered, activation link sent successfully!"
                }
            else:
                response["success"] = False
                response['message']= "User already registered!"
        except Exception as e:
            response = response
        return response

    def activation(self, token):
        try:
            response = {
                "success": False,
                "message": "Your account is not activate!"
            }
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = payload('id')
            data ={
                'id': user_id,
                'is_active': True
            }
            db_obj.update(table_name='users', data=data)
            response = {
                'success': True,
                "message":  "Your account is activated successfully!"
            }
        except Exception as e:
            response = response
        return response

    def loggined(self, user_data):
        try:
            response = {
                "success": False,
                "message": "Unable to login"
            }
            user_email = user_data['email']
            user_password = user_data['password']
            read_data = db_obj.read(table_name="users", column_name=None, column_value=None)
            for data in read_data:
                user_id, username, email, password, is_active = data
                if email == user_data['email'] and password == user_password and is_active == 1:
                    token = jwt.encode({'id': user_id}, 'secret', algorithm='HS256').decode('utf-8')
                    redis_obj.set(user_id, token)
                    response = {
                        "success": True,
                        "message": "Successfully logged in!",
                        "data": [token]
                    }
        except Exception as e:
            response = response
        return response

    def loggedout(self, that=None):
        try:
            response = {
                "success": False,
                "message": "Unable to logout",
                "data": []
            }
            token = that.headers['token']
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = payload.get('id')
            redis_obj.get(user_id)
            redis_obj.delete(user_id)
            response = {
                "success": True,
                "message": "Successfully logged out!"
            }
        except Exception as e:
            response = response
        return response

    def forgot_password(self, user_data,  that=None):
        try:
            response = {
                "success": False,
                "message": "Email not found!",
                "data": []
            }
            user_email = user_data['email']
            read_data = db_obj.read(table_name="users", column_name="email", column_value=user_email)
            if read_data == []:
                response['message'] = "This user is not registered"

            else:
                user_id = read_data[0][0]
                token = jwt.encode({'id': user_id}, 'secret', algorithm='HS256').decode('utf-8')
                host = that.headers['Host']
                protocol = that.protocol_version.split('/')[0].lower()
                message = f"Click on the link below to reset your password: {protocol}://{host}/reset/?token={token}"
                SMTP_Mail().do_mailing(user_email, message)
                response = {
                    "success": True,
                    "message": "Successfully sent link on your mail!",
                    "data": []
                }
        except Exception as e:
            response = response
        return response

    def reset_password(self, token, user_data):
        try:
            response = {
                "success": False,
                "message": "User not found!",
                "data": []
            }
            user_password = user_data['password']
            # token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6Nn0.NZbwdByCHPlxXpTYmB0ZdiY-kb2DMy4-vnarVBD1lFA"
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = payload.get('id')
            data = {
                "id": user_id,
                "password": user_password
            }
            db_obj.update(table_name="users", data=data)
            response = {
                "success": True,
                "message": "User password is reset successfully!"
            }
        except Exception as e:
            response = response
        return response

    def profile(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong"
            }
            ctype, pdict = cgi.parse_header(that.headers['content-type'])
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")

            if ctype == 'multipart/form-data':
                form = cgi.FieldStorage(fp=that.rfile, headers=that.headers, environ={'REQUEST_METHOD': 'POST',
                                        'CONTENT_TYPE': that.headers['Content-Type']})


                filename = form['upfile'].filename
                print(filename)
                data = form['upfile'].file.read()

                open("./media/%s" % filename, "wb").write(data)
                path = f"./media/{filename}"
                token = that.headers['token']
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                user_id = payload['id']
                data = {
                    "path": path,
                    "user_id": user_id
                }
                db_obj.insert(data=data, table_name="profile")

                response = {
                    "success": True,
                    "message": "profile upload successfully"
                }
        except Exception as e:
            response = response
        return response

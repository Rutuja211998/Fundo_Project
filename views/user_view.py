"""
This file contain user validations in which register, login, active, logot, forgot password validations are presents.
Author: Rutuja Tikhile.
Date: 12/3/2020
"""
import json
import cgi
from util import validate_email


class User:

    def register(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }
            # import pdb
            # pdb.set_trace ()
            form = cgi.FieldStorage(fp=that.rfile, headers=that.headers, environ={'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': that.headers['Content-Type']})
            form_keys = list(form.keys())
            username = form['username'].value
            email = form['email'].value
            password = form['password'].value

            if len(username) == 0:
                response['message'] = 'username can not be empty'
                raise ValueError

            if isinstance(username, (int)) or username.isdigit():
                response['message'] = 'username must be string'
                raise TypeError

            if not validate_email(email):
                response['message'] = 'not a valid email'
                return response

            if len(password) == 0:
                response['password'] = 'password cannot be blank'
                return response

            data = {}
            data['username'], data['email'], data['password'] = username, email, password
            response['success'] = True
            response['data'] = [data]
        except ValueError:
            response = response

        except TypeError:
            response = response

        except Exception as e:
            response = response

        return response

    def login(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }
            form = cgi.FieldStorage(fp=that.rfile, headers=that.headers, environ={'REQUEST_METHOD': 'POST',
                                                                                  'CONTENT_TYPE': that.headers[
                                                                                      'Content-Type']})
            form_keys = list(form.keys())
            data = {}
            email = form['email'].value
            password = form['password'].value

            if not validate_email(email):
                response['message'] = 'not a valid email'
                return response

            if len(password) == 0:
                response['password'] = 'password cannot be blank'
                return response
            data = {}
            data['email'], data['password'] = email, password
            response['success'] = True
            response['data'] = [data]
        except Exception as e:
            response = response
        return response

    def logout(self):
        response = {
                "success": True,
                "message": "User is logout"
            }
        return response

    def forgot_psd(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong, password not reset",
                "data": []
            }
            form = cgi.FieldStorage(fp=that.rfile, headers=that.headers, environ={'REQUEST_METHOD': 'POST',
                                                                                  'CONTENT_TYPE': that.headers[
                                                                                      'Content-Type']})
            form_keys = list(form.keys())
            data = {}
            email = form['email'].value

            if not validate_email(email):
                response['message'] = 'not a valid email'
                return response

            data = {}
            data['email'] = email
            response['success'] = True
            response['data'] = [data]
        except Exception as e:
            response = response
        return response

    def reset_psd(self, that=None):
        # import pdb
        # pdb.set_trace()
        try:
            response = {
                "success": False,
                "message": "something went wrong, password not reset"
            }
            form = cgi.FieldStorage(fp=that.rfile, headers=that.headers, environ={'REQUEST_METHOD': 'POST',
                                                                                  'CONTENT_TYPE': that.headers[
                                                                                      'Content-Type']})
            form_keys = list(form.keys())
            password = form['password'].value

            if password == 0:
                response['message'] = "password cannot be empty"
                raise ValueError

            data = {}
            data['password'] = password
            response['success'] = True
            response['data'] = [data]
        except ValueError:
            response = response

        except Exception as e:
            response = response

        return response

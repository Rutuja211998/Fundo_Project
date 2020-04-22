"""
This file contain class for notes which contains create, read, update and delete also for archive, pin and trash functions,
Author: Rutuja Tikhile.
Date: 16/3/2020
"""
import jwt
import json
from response import Response


class Notes:

    def create_note(self, that=None):
        try:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }
            content_length = int(that.headers['Content-Length'])
            body = that.rfile.read(content_length)
            request_data = json.loads(body)

            token = that.headers['token']
            payload = jwt.decode (token, 'secret', algorithms=['HS256'])
            user_id = payload['id']
            request_data['user_id'] = user_id
            response['success'], response['data'], response['message'] = True, [request_data], "valid data"
        except Exception as e:
            print(e)
            response = response
        return response

    def read_note (self, that=None):
        token = that.headers['token']
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user_id = payload['id']
        response = {
            'success': True,
            "data": [user_id],
            "message": "valid"
        }
        return response


    def update_note (self, that=None):
            content_length = int(that.headers['Content-Length'])
            body = that.rfile.read(content_length)
            request_data = json.loads(body)
            response = {
                'success': True,
                "data": [request_data],
                "message": "valid data"
            }
            return response

    def delete_note (self, that=None):
        content_length = int(that.headers['Content-Length'])
        body = that.rfile.read(content_length)
        request_data = json.loads(body)
        response = {
            'success': True,
            "data": [request_data],
            "message": "valid data"
        }
        return response

    def archive(self, that=None):
        content_length = int(that.headers['Content-Length'])
        body = that.rfile.read(content_length)
        request_data = json.loads(body)
        response = {
            'success': True,
            "data": [request_data],
            "message": "valid data"
        }
        return response

    def pinned(self, that=None):
        content_length = int(that.headers['Content-Length'])
        body = that.rfile.read(content_length)
        request_data = json.loads(body)
        response = {
            'success': True,
            "data": [request_data],
            "message": "valid data"
        }
        return response

    def trashed(self, that=None):
        content_length = int(that.headers['Content-Length'])
        body = that.rfile.read(content_length)
        request_data = json.loads(body)
        response = {
            'success': True,
            "data": [request_data],
            "message": "valid data"
        }
        return response

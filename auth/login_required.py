"""
This file having verification of tokens for the logged in users.
Author: Rutuja Tikhile.
Date:10/3/2020
"""
from response import Response
import jwt
from config.redis_connection import RedisCon
redis_object = RedisCon()

response = {
    'message': "something went wrong"
}

def login_required(method):
    def token_verification (self):
        try:
            response = {
                "success": False,
                "message": "something went wrong!",
                "data": []
            }
            print ( self.path, type ( self.path ) )
            if self.path not in ['/register', '/login', '/logout', '/activate', '/forgot_password']:
                token = self.headers['token']
                print ("tokenn  ",token)
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                key = payload['id']
                token = redis_object.get(key)
                if token is None:
                    raise ValueError("You Need To Login First")
                return method (self)
            else:
                return method (self)
        except jwt.DecodeError:
            response['message'] = "decode error"
            Response ( self ).jsonResponse ( status=400, data=response )

    return token_verification

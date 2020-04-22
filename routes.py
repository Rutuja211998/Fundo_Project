"""
This is the file which contains routes for all the user and note services.
Author: Rutuja Tikhile
Date: 28/02/2020
"""
from http.server import BaseHTTPRequestHandler
from views.user_view import User
from views.notes_view import Notes
from auth.login_required import login_required
from services.user_services import UserService
from services.note_services import Notes_API
from response import Response
from auth.login_required import login_required
from urllib.parse import urlparse


class Server(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    # GET Method
    def do_GET(self):
        if self.path == '/register':
            with open(r'./templates/register.html') as f:
                file = f.read()
                Response(self).html_response(status=200, data=file)

        if self.path == '/login':
            with open(r'./templates/login.html') as f:
                file = f.read()
                Response(self).html_response(status=200, data=file)

        if self.path == '/forgot_password':
            with open(r'./templates/forgot.html') as f:
                file = f.read()
                Response(self).html_response(status=200, data=file)

        if self.path == '/reset_password':
            with open(r'./templates/reset.html') as f:
                file = f.read()
                Response(self).html_response(status=200, data=file)

        if self.path == '/logout':
            pass

        if self.path == '/listing_archive':
            response = Notes_API().listing_archive()
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/listing_pin':
            response = Notes_API().listing_pin()
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/listing_trash':
            response = Notes_API().list_trash()
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/read_note':
            response = Notes().read_note(that=self)
            if response['success']:
                user_id = response['data'][0]
                response = Notes_API().reads(user_id)
            Response(self).jsonResponse(status=200, data=response)

    # POST Method
    @login_required
    def do_POST(self):
        response = {
                "success": False,
                "message": "Something went wrong!",
                "data": []
            }

        is_matched = self.path.split('/?')[0]
        if is_matched == '/activate':
            query = urlparse (self.path).query
            query_components = dict(qc.split ("=") for qc in query.split ("&"))
            print (query_components, "query_components----->", query)

            if query_components['token']:
                self.path = '/activate'

        elif self.path == '/register':
            response = User().register(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = UserService().registration(user_data, that=self)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/activate':
            response = UserService().activation(token=query_components['token'])
            Response(self).jsonResponse(status=200, data=response)

        elif self.path == '/login':
            response = User().login(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = UserService().loggined(user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/logout':
            response = User().logout()
            if response['success']:
                response = UserService().loggedout(that=self)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/forgot_password':
            response = User().forgot_psd(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = UserService().forgot_password(that=self, user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        is_matched = self.path.split('/?')[0]
        if is_matched == '/reset_password':
            query = urlparse(self.path).query
            query_components = dict(qc.split("=") for qc in query.split("&"))
            print(query_components, "query_components----->", query)

            if query_components['token']:
                self.path = '/reset_password'
        if self.path == '/reset_password':
            response = User().reset_psd(that=self)
            if response['success']:
                user_data = response['data'][0]
                response = UserService().reset_password(token=query_components['token'], user_data=user_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/create_note':
            print("debug")
            response = Notes().create_note(that=self)
            if response['success']:
                note_data = response['data'][0]
                response = Notes_API().create(note_data=note_data)
            Response (self).jsonResponse (status=200, data=response)

        if self.path == '/profile':
            response = UserService().profile(that=self)
        return Response(self).jsonResponse(status=200, data=response)

    # PUT Method
    @login_required
    def do_PUT (self):
        response = {
                "success": False,
                "message": "Something went wrong!",
                "data": []
        }

        if self.path == '/update_note':
            response = Notes().update_note(that=self)
            if response['success']:
                user_note = response['data'][0]
                response = Notes_API().update(user_note)
            Response (self).jsonResponse (status=200, data=response)

        if self.path == '/is_archived':
            response = Notes().archive(that=self)
            if response['success']:
                note_data = response['data'][0]
                response = Notes_API().archive(note_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/is_pinned':
            response = Notes().pinned(that=self)
            if response['success']:
                note_data = response['data'][0]
                response = Notes_API().pinned(note_data)
            Response(self).jsonResponse(status=200, data=response)

        if self.path == '/is_trashed':
            response = Notes().trashed(that=self)
            if response['success']:
                note_data = response['data'][0]
                response = Notes_API().trashed(note_data)
            Response(self).jsonResponse(status=200, data=response)

    # DELETE Method
    @login_required
    def do_DELETE(self):
        if self.path == '/delete_note':
            response = Notes().delete_note(that=self)
            if response['success']:
                user_note = response['data'][0]
                response = Notes_API().delete(user_note)
            Response (self).jsonResponse(status=200, data=response)
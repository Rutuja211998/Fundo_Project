"""
This file contains Notes_API class in which create, read, update and delete methods are present.
Author: Rutuja Tikhile.
Date:11/3/2020
"""
import jwt
from model.db_query import Query
db_obj = Query()
from response import Response


class Notes_API:
    # Insert data for creating note
    def create(self, note_data):
        try:
            db_obj.insert(data=note_data, table_name='notes')
            response = {
                    "success": True,
                    "message": "note created successfully!",
            }
        except Exception as e:
            response = response
        return response

    # Read data by giving specific id
    def reads(self, user_id):
        try:
            read_data = db_obj.read(table_name='notes', column_name='user_id', column_value=user_id)
            response = {
                'success': True,
                "data": [read_data],
                "message": "Read Successfully"
            }
        except Exception as e:
            response = response
        return response

    # Update data for the specific id
    def update(self, user_note):
        try:
            response = {
                'success': False,
                'message': "something went wrong"
            }
            column_val= user_note['id']
            updated_data = db_obj.update(table_name='notes', data=user_note)
            response = {
                'success': True,
                "data": [updated_data],
                "message": "Updated Successfully"
            }
        except Exception as e:
            response = response
        return response

    # Delete data for the specific id
    def delete(self, user_note):
        try:
            response = {
                'success': False,
                'message': "something went wrong"
            }
            note_id = user_note['id']
            db_obj.delete_note(table_name='notes', delete_id=note_id)
            response = {
                'success': True,
                "message": "Deleted Successfully"
            }
        except Exception as e:
            response = response
        return response

    # Here record is archived in table and response is shown.
    def archive(self, user_note):
        try:
            response = {
                'success': False,
                'message': "something went wrong"
            }
            column_val = user_note['is_archived']
            archived_data = db_obj.update(table_name='notes', data=user_note)
            response = {
                'success': True,
                "message": "Archived Successfully"
            }
        except Exception as e:
            response=response
        return response

    # Here record is pinned in table and response is shown.
    def pinned(self, user_note):
        try:
            response = {
                'success': False,
                'message': "something went wrong"
            }
            column_val = user_note['is_pinned']
            pinned_data = db_obj.update(table_name='notes', data=user_note)
            response = {
                'success': True,
                "message": "Pinned Successfully"
            }
        except Exception as e:
            response=response
        return response

    # Here record is trash in table and response is shown.
    def trashed(self, user_note):
        try:
            response = {
                'success': False,
                'message': "something went wrong"
            }
            column_val = user_note['is_trashed']
            trashed_data = db_obj.update(table_name='notes', data=user_note)
            response = {
                'success': True,
                "message": "Trashed Successfully"
            }
        except Exception as e:
            response=response
        return response

    def listing_archive(self):
        try:
            response = {
                "success": False,
                "message": "something went wrong!",
                "data": []
            }
            read_data = db_obj.read(table_name='notes', column_value=None, column_name=None)
            list = []
            for data in read_data:
                is_archived = data[6]
                if is_archived == 1:
                    list.append(data)
                    response = {
                        "success": True,
                        "message": "read archived successfully",
                        "data": [list]
                    }
        except Exception as e:
            response=response
        return response

    def listing_pin(self):
        try:
            response = {
                "success": False,
                "message": "something went wrong!",
                "data": []
            }
            read_data = db_obj.read(table_name='notes', column_value=None, column_name=None)
            list = []
            for data in read_data:
                if data[5] == 1:
                    list.append(data)
                    response = {
                        "success": True,
                        "message": "read pinned notes successfully",
                        "data": [list]
                    }
        except Exception as e:
            response = response
        return response

    def list_trash(self):
        try:
            response = {
                "success": False,
                "message": "something went wrong!",
                "data": []
            }
            read_data = db_obj.read(table_name='notes', column_value=None, column_name=None)
            list = []
            for data in read_data:
                if data[7] == 1:
                    list.append(data)
                    response = {
                        "success": True,
                        "message": "read trashed notes successfully",
                        "data": [list]
                    }
        except Exception as e:
            response=response
        return response
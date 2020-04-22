"""
This file contains test cases for users services.
Author: Rutuja Tikhile
Date:7/3/2020
"""
import requests
import json
baseurl = 'http://127.0.0.1:8000'


def test_user_registration():
    url = baseurl + '/register'
    user_data = {"username": "khali", "email": "zarbadeshruti8@gmail.com", "password": "1234"}
    headers = {'content-Type': "application/json"}
    response = requests.post(url=url, data=json.dumps(user_data), headers=headers)
    print(response.text)
    assert response.status_code


def test_user_login ():
    url = baseurl + '/login'
    user_data = {"username": "khali", "email": "zarbadeshruti8@gmail.com", "password": "1234"}
    headers = {'content-Type': "application/json"}
    response = requests.post ( url=url, data=json.dumps ( user_data ), headers=headers )
    print ( response.text )
    assert response.status_code


def test_user_logout():
    url = baseurl + '/logout'
    user_data = {"username": "khali", "email": "zarbadeshruti8@gmail.com", "password": "1234"}
    headers = {'content-Type': "application/json"}
    response = requests.post ( url=url, data=json.dumps ( user_data ), headers=headers )
    print ( response.text )
    assert response.status_code

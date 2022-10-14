
"""
auth handles all the requests that are related to authentication. 
"""
import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from .AuthHandler.signup_handler import signup
from .firebase_init import *


async def customer_login(request: HttpRequest):
    
    request_body = json.loads(request.body.decode("utf-8"))
    user = auth.verify_id_token(request_body["id_token"])
    user_id = user["uid"]


async def customer_signup(request: HttpRequest):

    request_body = json.loads(request.body.decode("utf-8"))
    return await signup(request_body["userdata"], request_body["password"], "customer")


async def provider_signup(request: HttpRequest):

    request_body = json.loads(request.body.decode("utf-8"))
    return await signup(request_body["userdata"], request_body["password"], "provider")

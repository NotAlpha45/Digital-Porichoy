
"""
auth handles all the requests that are related to authentication. 
"""
import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from .AuthHandler.signup_handler import signup


async def customer_login(request: HttpRequest):
    
    request_body = json.loads(request.body.decode("utf-8"))
    print(request_body["name"])
    return HttpResponse(""" 
    <h1>Customer login</h1>
    """)


async def customer_signup(request: HttpRequest):
    
    request_body = json.loads(request.body.decode("utf-8"))
    print(request_body)
    return await signup(request_body["userdata"], request_body["password"])
    

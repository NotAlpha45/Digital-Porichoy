
"""
auth handles all the requests that are related to authentication. 
"""
import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from .AuthHandler.signup_handler import signup
from .firebase_init import *
import hashlib


async def customer_login(request: HttpRequest):

    request_body = json.loads(request.body.decode("utf-8"))

    phone = request_body["phone"]
    password = request_body["password"]

    hash_obj = hashlib.new('sha512')
    hash_obj.update(password.encode('utf-8'))
    password = hash_obj.hexdigest()

    query = customers_collection.where("credentials.phone", "==", phone).where(
        "credentials.password", "==", password).limit(1).stream()

    customer = [x.to_dict() for x in query]

    if customer:
        user_id = auth.get_user_by_phone_number(phone).uid
        
        print(auth.create_custom_token(user_id))
        
        return JsonResponse({
            "userId": user_id,
            "role": "customer"
        })
    else:
        return JsonResponse({
            "userId": None
        })


async def customer_signup(request: HttpRequest):

    request_body = json.loads(request.body.decode("utf-8"))
    return await signup(request_body["userdata"], request_body["password"], "customer")


async def provider_signup(request: HttpRequest):

    request_body = json.loads(request.body.decode("utf-8"))
    return await signup(request_body["userdata"], request_body["password"], "provider")

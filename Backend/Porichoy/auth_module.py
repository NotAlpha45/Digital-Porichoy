
"""
auth handles all the requests that are related to authentication. 
"""
import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from .AuthHandler.signup_handler import signup
from .firebase_init import *
import hashlib
from .models import ImageStore


def update_user_image(request: HttpRequest):
    image = request.FILES["content"]
    name = request.POST["filename"]

    image_store_obj = ImageStore(image_name=name, image_content=image)
    image_store_obj.save()

    verified_obj = auth.verify_id_token(request.POST["token"])
    current_user_id = verified_obj["uid"]
    current_user_role = request.POST["role"]

    current_collection = None

    if current_user_role == "customer":
        current_collection = customers_collection
    elif current_user_role == "provider":
        current_collection = providers_collection

    user_instance = current_collection.document(current_user_id)
    # print(user_instance)
    user_instance.update({
        "credentials.image_url": name
    })

    return HttpResponse(200)


async def update_user_info(request: HttpRequest):
    request_body = json.loads(request.body.decode("utf-8"))
    verified_obj = auth.verify_id_token(request_body["token"])

    current_user_id = verified_obj["uid"]
    current_user_role = request_body["role"]

    new_name = request_body["name"]
    new_username = request_body["username"]
    new_phone = request_body["phone"]
    password = request_body["password"]

    current_collection = None

    if current_user_role == "customer":
        current_collection = customers_collection
    elif current_user_role == "provider":
        current_collection = providers_collection

    user_instance = current_collection.document(current_user_id)

    user_instance.update({

        "names.username": new_username,
        "names.name": new_name,
        "credentials.phone": new_phone

    })

    if password != "":
        hash_obj = hashlib.new('sha512')
        hash_obj.update(request_body["password"].encode('utf-8'))
        password = hash_obj.hexdigest()

        auth.update_user(
            current_user_id,
            phone_number=request_body["phone"],
            password=password
        )

        user_instance.update({


            "credentials.password": password

        })

    else:
        auth.update_user(
            current_user_id,
            phone_number=request_body["phone"]
        )

    return JsonResponse({
        "status": "ok"
    })


async def get_user_info(request: HttpRequest):
    request_body = json.loads(request.body.decode("utf-8"))
    verified_obj = auth.verify_id_token(request_body["token"])
    current_user_id = verified_obj["uid"]
    # print("here is my obj", verified_obj["uid"])

    # Search in both customer and provider collection, as the user may be anyone
    current_customer_data = customers_collection.document(
        current_user_id).get()
    current_provider_data = providers_collection.document(
        current_user_id).get()

    if current_customer_data.exists:
        return JsonResponse(current_customer_data.to_dict())
    elif current_provider_data.exists:
        return JsonResponse(current_provider_data.to_dict())


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

        user_id_token = auth.create_custom_token(user_id).decode('utf-8')

        return JsonResponse({
            "userId": user_id_token,
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


"""
services handles all the requests that are related to services. 
"""
import json
from unittest import result
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from .firebase_init import *
from .models import ImageStore


async def create_service(request: HttpRequest):

    service_data = json.loads(request.body.decode("utf-8"))

    try:
        user_id = auth.get_user(service_data["credentials"]["provider_id"]).uid

        service_instance = services_collection.document(user_id).get()

        if not service_instance.exists:
            services_collection.document(user_id).set(service_data)

            return JsonResponse(
                {
                    "provider_id": service_data["credentials"]["provider_id"]
                }
            )
        else:
            return JsonResponse(
                {
                    "provider_id": "exists"
                }
            )

    except auth.UserNotFoundError:
        return JsonResponse(
            {
                "provider_id": None
            }
        )


def add_offering(request: HttpRequest):

    request_body = request.POST
    verified_obj = auth.verify_id_token(request_body["user_token"])
    service_id = verified_obj["uid"]

    offering_name = request_body["offering_name"]
    offering_price = request_body["offering_price"]
    offering_description = request_body["offering_description"]
    offering_image_url = request_body["offering_image_url"]
    offering_image = request.FILES["offering_image"]

    service_instance = services_collection.document(service_id)
    service_data = service_instance.get()

    if service_data.exists:
        image_store_obj = ImageStore(
            image_name=offering_image_url, image_content=offering_image)
        image_store_obj.save()
        service_instance.update({
            "offerings": firestore.ArrayUnion([{
                "offering_name": offering_name,
                "offering_description": offering_description,
                "offering_price": offering_price,
                "offering_image_url": offering_image_url
            }])
        })
        return JsonResponse({
            "status": "ok"
        })
    else:
        return JsonResponse({
            "status": "unavailable"
        })


async def get_offerings(request: HttpRequest):
    request_body = request.GET
    verified_obj = auth.verify_id_token(request_body["user_token"])
    service_id = verified_obj["uid"]

    service_instance = services_collection.document(service_id)
    service_data = service_instance.get().to_dict()

    offering_data = list(service_data["offerings"])

    return JsonResponse({
        "offerings": offering_data
    })


def remove_offering(request: HttpRequest):

    request_body = json.loads(request.body.decode("utf-8"))

    verified_obj = auth.verify_id_token(request_body["user_token"])
    service_id = verified_obj["uid"]

    deleted_offering = request_body["deleted_offering"]

    service_instance = services_collection.document(service_id)
    service_data = service_instance.get()

    if service_data.exists:
        service_instance.update({
            "offerings": firestore.ArrayRemove([deleted_offering])
        })
        ImageStore.objects.filter(
            image_name=deleted_offering["offering_image_url"]).delete()
        return JsonResponse({
            "status": "ok"
        })
    else:
        return JsonResponse({
            "status": "unavailable"
        })


async def get_my_service(request: HttpRequest):
    request_params = request.GET

    verified_obj = auth.verify_id_token(request_params["user_token"])

    service_id = verified_obj["uid"]

    result = services_collection.document(service_id).get().to_dict()

    response_data = {
        "result": result
    }

    return JsonResponse(response_data)


async def get_service_by_id(request: HttpRequest):
    request_params = request.GET

    service_id = request_params["service_id"]

    result = services_collection.document(service_id).get().to_dict()

    response_data = {
        "result": result
    }

    return JsonResponse(response_data)


async def search_service(request: HttpRequest):

    """
    Searches for a service based on category and location. 
    """

    request_params = request.GET
    district = request_params["district"].lower()
    category = request_params["category"].lower()
    customer_long = float(request_params["long"])
    customer_lat = float(request_params["lat"])
    distance = float(request_params["distance"])
    search_limit = int(request_params["search_limit"])

    # Setting max search limit and max distance limit.
    if search_limit > 1000:
        search_limit = 1000

    if distance > 50:
        distance = 50

    query = services_collection.where(
        "location.district", "==", district).where("credentials.category", "==", category).limit(search_limit).stream()

    result = [x.to_dict() for x in query]

    # Only taking the instances who's distance is less than or equal to the specified distance
    result = [x for x in result if (((x["location"]["long"] - customer_long)**2 +
                                     (x["location"]["lat"] - customer_lat)**2)**0.5)*111 <= distance]

    result.sort(key=lambda x: (
        (((x["location"]["long"] - customer_long)**2 +
         (x["location"]["lat"] - customer_lat)**2)**0.5)
    ))

    response_data = {
        "result": result
    }

    return JsonResponse(response_data)

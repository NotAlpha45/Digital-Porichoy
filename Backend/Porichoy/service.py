
"""
services handles all the requests that are related to services. 
"""
import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from .ServiceHandler.service_handler import create_service


async def create_service(request: HttpRequest):

    request_body = json.loads(request.decode("utf-8"))
    print(type(request_body))
    # print(type(json.loads(request.body.decode("utf-8"))))
    return HttpResponse("OK")
    # return await create_service(request_body)

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from .models import ImageStore
from base64 import b64encode


def save_image(request: HttpRequest):
    image = request.FILES["content"]
    name = request.POST["filename"]
    image_store_obj = ImageStore(image_name=name, image_content=image)
    image_store_obj.save()

    return JsonResponse({
        "status": "ok"
    })


def get_image(request: HttpRequest):

    name = request.GET["filename"]

    response = HttpResponse(ImageStore.objects.get(
        image_name=name).image_content.read(), content_type="image/jpeg")

    return response

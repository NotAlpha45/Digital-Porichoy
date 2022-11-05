from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from .models import ImageStore


def save_image(request: HttpRequest):
    image = request.FILES["content"]
    name = request.POST["filename"]
    print(image)
    image_store_obj = ImageStore(image_name=name, image_content=image)
    image_store_obj.save()

    return HttpResponse("""
    ok
    """)

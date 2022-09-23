from django.urls import path
from . import auth
from . import service

urlpatterns = [
    path('customer_auth/login', auth.customer_login),
    path('customer_auth/signup', auth.customer_signup),
    path('provider_auth/signup', auth.provider_signup),
    path('create_service', service.create_service)
]

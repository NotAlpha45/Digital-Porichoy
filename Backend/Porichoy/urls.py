from django.urls import path
from . import auth

urlpatterns = [
    path('customer_auth/login', auth.customer_login),
    path('customer_auth/signup', auth.customer_signup)
]

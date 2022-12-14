from django.urls import path
from . import auth_module
from . import service
from . import image

urlpatterns = [
    path('customer_auth/login', auth_module.customer_login),
    path('customer_auth/signup', auth_module.customer_signup),
    path('provider_auth/signup', auth_module.provider_signup),
    path('create_service', service.create_service),
    path('add_offering', service.add_offering),
    path('remove_offering', service.remove_offering),
    path('search_service', service.search_service),
    path('get_service', service.get_service_by_id),
    path('get_user', auth_module.get_user_info),
    path('update_user', auth_module.update_user_info),
    path('update_user_image', auth_module.update_user_image),
    path('save_image', image.save_image),
    path('get_image', image.get_image),
    path('get_offerings', service.get_offerings),
    path('get_my_service', service.get_my_service),
    path('service_exists', service.service_exists),
    path('edit_service', service.edit_service),
    path("edit_service_image", service.edit_service_image)
]

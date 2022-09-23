from ..firebase_init import *


async def create_service(service_data):
    try:
        auth.get_user(service_data["credentials"]["provider_id"])
        services_collection.document(
            service_data["credentials"]["provider_id"]).set(service_data)

        return HttpResponse('''
        <h1>Your Service Created!</h1>
        ''')

    except auth.UserNotFoundError:
        return HttpResponse('''
        <h1>Not A valid provider!</h1>
        ''')

from ..firebase_init import *
from django.http import JsonResponse


async def signup(userdata, password, user_type: str):
    """
    Creates a firebase user instance and stores in the firestore database.
    """

    collection = None

    if user_type == "customer":
        collection = customers_collection
    elif user_type == "provider":
        collection = providers_collection

    user = None

    try:

        user = auth.create_user(
            email_verified=False,
            phone_number=userdata["credentials"]["phone"],
            password=password,
            display_name=userdata["names"]["username"],
            disabled=False)

        collection.document(user.uid).set(userdata)
        print(user)

        return HttpResponse(
            f'''
            <h1>Account Created for {userdata["names"]["username"]}!</h1>
            '''
        )

    except auth.PhoneNumberAlreadyExistsError:

        if user_type == "customer":
            print("Account already exists")
            return HttpResponse(
                '''
                <h1>User already exists</h1>
                '''
            )

        elif user_type == "provider":
            user = None

            user = auth.get_user_by_phone_number(
                userdata["credentials"]["phone"])

            provider_instance = providers_collection.document(user.uid).get()

            if not provider_instance.exists:

                collection.document(user.uid).set(userdata)
                return HttpResponse(
                    f'''
                <h1>Account Created for {userdata["names"]["username"]}!</h1>
                '''
                )
            else:
                return HttpResponse(
                    f'''
                <h1>The provider already exists</h1>
                '''
                )

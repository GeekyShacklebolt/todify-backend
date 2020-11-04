# Third Party Stuff
from django.contrib.auth import get_user_model


def create_user_account(username, email, password, **extra_fields):
    user = get_user_model().objects.create_user(
        username=username,
        email=email,
        password=password,
        **extra_fields
    )
    return user

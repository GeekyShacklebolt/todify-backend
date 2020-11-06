# Standard Library
import json

# Third Party Stuff
import pytest
from django.test import Client
from django.urls import reverse

# Todify Stuff
from todify.users import services

client = Client()
pytestmark = pytest.mark.django_db


def test_user_registration(client):
    url = reverse("auth-register")
    credentials = {
        "username": "testuser",
        "email": "test@test.com",
        "password": "localhost",
    }
    response = client.post(url, credentials)
    assert response.status_code == 201
    expected_keys = [
        "id", "username", "email", "first_name", "last_name", "avatar", "last_login", "created_at"
    ]

    assert set(expected_keys).issubset(response.data.keys())
    assert response.data["email"] == "test@test.com"
    assert response.data["username"] == "testuser"


def test_list_users(client):
    credentials = {
        "username": "testuser",
        "email": "test@test.com",
        "password": "localhost",
    }
    user = services.create_user_account(**credentials)

    url = reverse("users-list")
    response = client.get(url)

    assert response.status_code == 200
    assert response.data["count"] == 1  # since only 1 user is created in this test
    assert response.data["results"][0]["id"] == str(user.id)
    assert response.data["results"][0]["username"] == "testuser"
    assert response.data["results"][0]["email"] == "test@test.com"


def test_retrieve_user_by_id(client):
    credentials = {
        "username": "testuser",
        "email": "test@test.com",
        "password": "localhost",
    }
    user = services.create_user_account(**credentials)

    url = reverse("users-detail", kwargs={'pk': user.id})
    response = client.get(url)

    assert response.status_code == 200
    expected_keys = [
        "id", "username", "email", "first_name", "last_name", "avatar", "last_login", "created_at"
    ]
    assert set(expected_keys).issubset(response.data.keys())
    assert response.data["email"] == "test@test.com"
    assert response.data["username"] == "testuser"


def test_retrieve_user_by_username_as_query_param(client):
    credentials = {
        "username": "testuser",
        "email": "test@test.com",
        "password": "localhost",
    }
    user = services.create_user_account(**credentials)

    url = "{}?username={}".format(reverse("users-list"), credentials["username"])
    response = client.get(url)

    assert response.status_code == 200
    assert response.data["count"] == 1  # since only 1 user can be queried through query param
    assert response.data["results"][0]["id"] == str(user.id)
    assert response.data["results"][0]["username"] == "testuser"
    assert response.data["results"][0]["email"] == "test@test.com"


def test_get_profile_of_current_logged_in_user(client):
    credentials = {
        "username": "testuser",
        "email": "test@test.com",
        "password": "localhost",
    }
    user = services.create_user_account(**credentials)

    client.login(username=credentials["username"], password=credentials["password"])

    url = reverse("me-list")
    response = client.get(url)

    assert response.status_code == 200
    expected_keys = [
        "id", "username", "email", "first_name", "last_name", "avatar", "last_login", "created_at"
    ]
    assert set(expected_keys).issubset(response.data.keys())
    assert response.data["email"] == "test@test.com"
    assert response.data["username"] == "testuser"
    assert response.data["id"] == str(user.id)


def test_delete_profile_of_current_logged_in_user(client):
    credentials = {
        "username": "testuser",
        "email": "test@test.com",
        "password": "localhost",
    }
    user = services.create_user_account(**credentials)

    client.login(username=credentials["username"], password=credentials["password"])

    url = reverse("me-detail", kwargs={'pk': user.id})
    response = client.delete(url)

    assert response.status_code == 204
    assert response.data is None


def test_update_profile_of_current_logged_in_user(client):
    credentials = {
        "username": "testuser",
        "email": "test@test.com",
        "password": "localhost",
    }
    user = services.create_user_account(**credentials)

    client.login(username=credentials["username"], password=credentials["password"])
    url = reverse("me-list")
    response = client.get(url)

    assert response.status_code == 200
    assert response.data["id"] == str(user.id)

    assert response.data["first_name"] == ""
    assert response.data["last_name"] == ""

    patch_request_body = {
        "first_name": "Shiva",
        "last_name": "Saxena",
    }

    response = client.patch(url, json.dumps(patch_request_body), content_type='application/json')
    assert response.status_code == 200
    assert response.data["id"] == str(user.id)

    assert response.data["first_name"] == "Shiva"
    assert response.data["last_name"] == "Saxena"


def test_change_password_of_current_logged_in_user(client):
    credentials = {
        "username": "testuser",
        "email": "test@test.com",
        "password": "localhost",
    }
    services.create_user_account(**credentials)

    client.login(username=credentials["username"], password=credentials["password"])
    request_body = {
        "current_password": "localhost",
        "new_password": "hellohost",
    }
    url = reverse("me-password-change")
    response = client.post(url, request_body)

    assert response.status_code == 204
    assert response.data is None

    client.logout()
    login_response_with_old_password = client.login(
        username=credentials["username"], password=credentials["password"]
    )
    assert login_response_with_old_password is False

    login_response_with_new_password = client.login(
        username=credentials["username"], password=request_body["new_password"]
    )
    assert login_response_with_new_password is True


# TODO: add tests for the the following actions
# Update avatar of current logged in user
# Remove avatar of current logged in user

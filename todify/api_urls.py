# Third Party Stuff
from rest_framework import routers

# Todify Stuff
from todify.users.api import AuthUserViewset, CurrentUserViewset, UserViewset

default_router = routers.DefaultRouter(trailing_slash=False)

default_router.register("auth", AuthUserViewset, basename="auth")
default_router.register("users", UserViewset, basename="users")
default_router.register("me", CurrentUserViewset, basename="me")

urlpatterns = default_router.urls

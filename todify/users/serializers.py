# Third Party Stuff
from django.contrib.auth import password_validation
from rest_framework import serializers

from . import models


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["username", "email", "password"]


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context["request"].user.check_password(value):
            raise serializers.ValidationError("Incorrect current password!")
        return value

    def validate_new_password(self, value):
        # https://docs.djangoproject.com/en/2.0/topics/auth/passwords/#django.contrib.auth.password_validation.validate_password
        password_validation.validate_password(value)
        return value


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "avatar",
            "last_login",
            "created_at",
        ]
        read_only_fields = (
            "id",
            "created_at",
            "last_login",
        )


class CurrentUserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["avatar"]

# Standard Library
import uuid

# Third Party Stuff
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.postgres.fields import CIEmailField
from django.db import models
from uuid_upload_path import upload_to
from versatileimagefield.fields import PPOIField, VersatileImageField

# Todify Stuff
from todify.base.models import TimeStampedUUIDModel


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
        self,
        username: str,
        email: str,
        password: str,
        is_staff: str,
        is_superuser: str,
        **extra_fields,
    ):
        if "id" not in "extra_fields":
            extra_fields["id"] = uuid.uuid4()

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=True,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username: str, email: str, password=None, **extra_fields):
        """Creates and saves a User with the given username, email and password.
        """
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username: str, email: str, password=None, **extra_fields):
        return self._create_user(username, email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, TimeStampedUUIDModel):
    first_name = models.CharField(
        max_length=120, null=False, blank=True, default="", verbose_name="First Name",
    )
    last_name = models.CharField(
        max_length=120, null=False, blank=True, default="", verbose_name="Last Name",
    )
    email = CIEmailField(
        null=False, blank=False, unique=True, db_index=True, verbose_name="Email Address",
    )
    username = models.CharField(
        max_length=32, null=False, blank=False, unique=True, verbose_name="Username",
    )
    avatar = VersatileImageField(
        upload_to=upload_to, blank=True, null=True, ppoi_field="avatar_poi", verbose_name="Avatar",
    )
    avatar_poi = PPOIField(verbose_name="Avatar's Point of Interest")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
    is_active = models.BooleanField(
        verbose_name="Active Status",
        default=True,
        help_text="Designates whether this user should be treated as "
        "active. Unselect this instead of deleting accounts.",
    )
    is_staff = models.BooleanField(
        verbose_name="Staff Status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ("-created_at",)
        db_table = 'user'

    def __str__(self):
        if self.get_full_name():
            return f"{self.get_full_name()} ({self.username})"
        return str(self.username)

    def get_full_name(self) -> str:
        """Returns the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self) -> str:
        """Returns the short name for the user.
        """
        return self.first_name.strip()

# Third Party Stuff
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group

from .models import User


# ModelAdmins
# ----------------------------------------------------------------------------
@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    model = User
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "avatar",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    # "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "created_at", "modified_at")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2"
                ),
            },
        ),
    )
    readonly_fields = ("created_at", "last_login", "modified_at")
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
    )
    list_filter = ("is_superuser", "is_active")
    search_fields = ("first_name", "last_name", "email", "username")
    ordering = ("email", "username")


admin.site.unregister(Group)

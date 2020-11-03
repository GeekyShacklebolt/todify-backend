# Third Party Stuff
from django.contrib import admin

from . import models


@admin.register(models.Card)
class CardAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Primary Key", {
            "fields": ("id",),
        }),
        ("Card Info", {
            "fields": (
                "title",
                "description",
                "link",
                "created_by",
                "wishlist",
                "photo",
            ),
        }),
        ("Timestamps", {
            "fields": ("created_at", "modified_at"),
        }),
    )
    list_display = (
        "id",
        "title",
        "wishlist",
        "created_by",
    )
    list_filter = (
        "created_at",
    )
    readonly_fields = (
        "id",
        "created_at",
        "modified_at",
        "photo_poi",
    )
    search_fields = (
        "title",
        "wishlist__title",
        "created_by__username",
    )
    ordering = (
        "created_at",
    )

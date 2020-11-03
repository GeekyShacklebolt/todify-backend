# Third Party Stuff
from django.contrib import admin

from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Primary Key", {
            "fields": ("id",),
        }),
        ("Card Info", {
            "fields": (
                "title",
                "description",
                "rating",
                "created_by",
                "card",
                "will_recommend",
            ),
        }),
        ("Timestamps", {
            "fields": ("created_at", "modified_at"),
        }),
    )
    list_display = (
        "id",
        "title",
        "rating",
        "card",
        "created_by",
        "will_recommend",
    )
    list_filter = (
        "created_at",
        "will_recommend",
        "rating",
    )
    readonly_fields = (
        "id",
        "created_at",
        "modified_at",
    )
    search_fields = (
        "title",
        "card__title",
        "created_by__username",
    )
    ordering = (
        "created_at",
    )

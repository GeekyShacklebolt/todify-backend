# Third Party Stuff
from django.contrib import admin

from . import models


@admin.register(models.Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Primary Key', {
            "fields": ("id",),
        }),
        ('Wishlist Info', {
            'fields': ('title', 'description', 'is_public', 'created_by'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'modified_at'),
        }),
    )
    list_display = (
        "title",
        "created_by",
        "is_public",
    )
    list_filter = (
        "created_at",
        "is_public",
    )
    readonly_fields = (
        "id",
        "created_at",
        "modified_at",
    )
    search_fields = (
        "title",
        "created_by__username",
    )
    ordering = (
        "title",
        "created_at",
    )


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Primary Key', {
            "fields": ("id",),
        }),
        ('Category Info', {
            'fields': ('name', 'created_by'),
        }),
    )
    list_display = (
        "name",
        "created_by",
    )
    readonly_fields = (
        "id",
    )
    search_fields = (
        "name",
        "created_by__username",
    )
    ordering = (
        "name",
    )


@admin.register(models.WishlistCategoryMapping)
class WishlistCategoryMappingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Primary Key', {
            "fields": ("id",),
        }),
        ('Wishlist Category Mapping Info', {
            'fields': ('wishlist', 'category'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'modified_at'),
        }),
    )
    list_display = (
        "id",
        "wishlist",
        "category",
    )
    readonly_fields = (
        "id",
        "created_at",
        "modified_at",
    )
    search_fields = (
        "wishlist__title",
        "category__name",
    )
    ordering = (
        "created_at",
    )

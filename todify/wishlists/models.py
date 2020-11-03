# Third Party Stuff
from django.conf import settings
from django.db import models

# Todify Stuff
from todify.base.models import TimeStampedUUIDModel, UUIDModel


class Category(UUIDModel):
    name = models.CharField(
        max_length=120, null=False, blank=False, default="", verbose_name="Name",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="categories"
    )

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        db_table = 'category'

    def __str__(self):
        return f"{self.name}"


class Wishlist(TimeStampedUUIDModel):
    title = models.CharField(
        max_length=120, null=False, blank=False, default="", verbose_name="Title",
    )
    description = models.CharField(
        max_length=360, null=False, blank=True, default="", verbose_name="Description",
    )
    is_public = models.BooleanField(
        verbose_name="Visibility Status",
        default=True,
        help_text="Designates whether this wishlist should be treated as "
        "public. Any todify user can view a public wishlist.",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wishlists"
    )
    categories = models.ManyToManyField(
        Category,
        through="WishlistCategoryMapping",
        related_name="wishlists",
        through_fields=("wishlist", "category",),
    )

    class Meta:
        verbose_name = "wishlist"
        verbose_name_plural = "wishlists"
        ordering = ("-created_at",)
        db_table = 'wishlist'

    def __str__(self):
        return f"{self.title}"


class WishlistCategoryMapping(TimeStampedUUIDModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'wishlist_category_mapping'
        verbose_name_plural = "wishlist_category_mappings"
        unique_together = ("wishlist", "category")
        ordering = ("-created_at",)
        db_table = 'wishlist_category_mapping'

    def __str__(self):
        return f"{self.wishlist} - {self.category} - {self.created_at}"

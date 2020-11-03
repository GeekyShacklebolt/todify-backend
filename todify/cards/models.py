# Third Party Stuff
from django.conf import settings
from django.db import models
from uuid_upload_path import upload_to
from versatileimagefield.fields import PPOIField, VersatileImageField

# Todify Stuff
from todify.base.models import TimeStampedUUIDModel


class Card(TimeStampedUUIDModel):
    title = models.CharField(
        max_length=120, null=False, blank=False, default="", verbose_name="Title",
    )
    description = models.CharField(
        max_length=360, null=False, blank=True, default="", verbose_name="Description",
    )
    link = models.URLField(
        max_length=200, null=False, blank=False, default="", verbose_name="Link",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cards"
    )
    wishlist = models.ForeignKey(
        "wishlists.Wishlist", on_delete=models.CASCADE, related_name="cards"
    )
    photo = VersatileImageField(
        upload_to=upload_to, blank=True, null=True, ppoi_field="photo_poi", verbose_name="Avatar",
    )
    photo_poi = PPOIField(verbose_name="Photo's Point of Interest")

    class Meta:
        verbose_name = "card"
        verbose_name_plural = "cards"
        ordering = ("-created_at",)
        db_table = 'card'

    def __str__(self):
        return f"{self.title}"

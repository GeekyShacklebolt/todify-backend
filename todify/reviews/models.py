# Third Party Stuff
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Todify Stuff
from todify.base.models import TimeStampedUUIDModel


class Review(TimeStampedUUIDModel):
    title = models.CharField(
        max_length=120, null=False, blank=False, verbose_name="Title",
    )
    description = models.CharField(
        max_length=512, null=False, blank=True, default="", verbose_name="Description",
    )
    rating = models.IntegerField(
        null=True, blank=True, default=None, verbose_name="Rating",
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        help_text="Star rating 0 to 10",
    )
    will_recommend = models.BooleanField(
        verbose_name="Will Recommend", null=True, blank=True, default=None,
        help_text="Designates whether the user would like to recommend the card to others",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews"
    )
    card = models.ForeignKey(
        "cards.Card", on_delete=models.CASCADE, related_name="reviews"
    )

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"
        ordering = ("-created_at",)
        db_table = 'review'

    def __str__(self):
        return f"{self.title}"

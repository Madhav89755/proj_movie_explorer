from django.db import models
from django.utils.translation import gettext_lazy as _


class CommonModel(models.Model):
    """Abstract base model that provides common fields for all models."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_data = models.JSONField(blank=True, null=True)

    class Meta:
        abstract = True

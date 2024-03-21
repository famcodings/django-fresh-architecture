from django.contrib.auth.models import AbstractUser
from django.db import models
from django_fresh_architecture.base_models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):

    address = models.CharField(
        max_length=255,
        blank=True,
        default=None,
        null=True
    )
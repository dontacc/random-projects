from django.db import models
from core.models import AbstractBaseModel


class Wallet(AbstractBaseModel):
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=32)

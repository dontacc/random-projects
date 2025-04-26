from django.db import models
from core.models import AbstractBaseModel


class Wallet(AbstractBaseModel):
    class WalletType(models.TextChoices):
        PHYSICAL = "PHYSICAL", "PHYSICAL"
        DIGITAL = "DIGITAL", "DIGITAL"


    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    amount = models.BigIntegerField(default=0)
    type = models.CharField(max_length=64, choices=WalletType.choices, default=WalletType.DIGITAL)

from django.db import models
from authentication.models import User


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wallets")
    wallet_address = models.TextField()

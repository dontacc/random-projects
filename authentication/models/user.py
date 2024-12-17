from django.db import models
from core.models import AbstractBaseModel
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from authentication.utils import PhoneNumberValidator


class User(AbstractBaseModel, AbstractUser, PermissionsMixin):
    class Status(models.TextChoices):
        USER_A = "user_a", "USER_A"
        USER_B = "user_b", "USER_B"

    phone_number = models.CharField(max_length=32, validators=[PhoneNumberValidator])
    status = models.CharField(max_length=31, choices=Status.choices, default=Status.USER_A)

    def __str__(self):
        return self.phone_number

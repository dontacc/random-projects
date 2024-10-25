from django.db import models
from core.models import AbstractBaseModel
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from authentication.utils import PhoneNumberValidator


class User(AbstractBaseModel, AbstractUser, PermissionsMixin):
    phone_number = models.CharField(max_length=32, validators=[PhoneNumberValidator])

    def __str__(self):
        return self.phone_number

from django.db import models
from core.models import AbstractBaseModel
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from authentication.utils import PhoneNumberValidator
from django.core.exceptions import ValidationError


def validate_file_size(value):
    max_size = 8 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError("")


class User(AbstractBaseModel, AbstractUser, PermissionsMixin):
    class Status(models.TextChoices):
        USER_A = "user_a", "USER_A"
        USER_B = "user_b", "USER_B"

    phone_number = models.CharField(max_length=32, validators=[PhoneNumberValidator])
    status = models.CharField(max_length=31, choices=Status.choices, default=Status.USER_A)
    user_image = models.ImageField(upload_to="media/", validators=[validate_file_size])

    def __str__(self):
        return self.username

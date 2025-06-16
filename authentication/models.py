from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from core.models import AbstractBaseModel
from authentication import validators


class User(AbstractBaseModel, AbstractUser, PermissionsMixin):
    class Status(models.TextChoices):
        USER_A = "user_a", "USER_A"
        USER_B = "user_b", "USER_B"

    phone_number = models.CharField(max_length=32, validators=[validators.PhoneNumberValidator])
    status = models.CharField(max_length=31, choices=Status.choices, default=Status.USER_A)
    user_image = models.ImageField(upload_to="media/", validators=[validators.validate_file_size])

    def __str__(self):
        return self.username


class WalletType(models.TextChoices):
    PHYSICAL = "PHYSICAL", "PHYSICAL"
    DIGITAL = "DIGITAL", "DIGITAL"


class WalletQuerySet(models.QuerySet):
    def search(self, title=None):
        if title is None or title == "":
            return self.all()[:30]
        return self.filter(title__icontains=title)

    def active_wallets(self):
        return self.filter(is_active=True)


class SearchWalletManager(models.Manager):

    def search(self, title):
        if title is None or title == "":
            return self.none()
        return self.filter(title__icontains=title)


class Wallet(AbstractBaseModel):
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    amount = models.BigIntegerField(default=0)
    type = models.CharField(max_length=64, choices=WalletType.choices, default=WalletType.DIGITAL)
    is_active = models.BooleanField(default=True)
    icon = models.ImageField(upload_to="")

    objects = WalletQuerySet.as_manager()

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        pass


class WalletRevision(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    amount = models.BigIntegerField(default=0)
    type = models.CharField(max_length=64, choices=WalletType.choices, default=WalletType.DIGITAL)
    is_active = models.BooleanField(default=True)
    modified_at = models.DateTimeField()
    modified_by = models.DateTimeField()


class Book(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    author = models.ForeignKey("authentication.Author", on_delete=models.CASCADE)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE, related_name="ratings")
    rate_number = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.user.username


class Author(models.Model):
    name = models.CharField(max_length=32)

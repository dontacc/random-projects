from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Rating(models.Model):
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE, related_name="ratings")
    rate_number = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.user.username

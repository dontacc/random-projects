from django.db import models
import uuid


class Book(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    author = models.ForeignKey("authentication.Author", on_delete=models.CASCADE)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

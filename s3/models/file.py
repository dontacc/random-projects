from django.db import models


class File(models.Model):
    file = models.FileField(upload_to="media/")
    is_on_s3 = models.BooleanField(default=False)
    is_on_local = models.BooleanField(default=False)

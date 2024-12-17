# from django.db import models
#
#
# class File(models.Model):
#     file = models.FileField(upload_to="media/")
#     is_on_s3 = models.BooleanField(default=False)
#     is_on_local = models.BooleanField(default=False)
#
#
# def upload_to_address(instance, file_name):
#     return
#
#
# class Test(models.Model):
#     user = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
#     file = models.FileField(upload_to=upload_to_address)

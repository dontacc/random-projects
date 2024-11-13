from django.contrib import admin
from .file import FileAdmin
from s3.models import File

admin.site.register(File, FileAdmin)

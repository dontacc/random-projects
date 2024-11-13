import os
import django
import os
import sys
from django.core.files.storage import storages

# sys.path.append('//')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_authentication.settings')
# django.setup()
from s3.models import File
from celery import shared_task


@shared_task
def check_s3_and_local():
    files = File.objects.all()
    s3_storage = storages["default"]
    local_storage = storages["local"]
    for file in files:
        if s3_storage.exists(file.file.name):
            file.is_on_s3 = True
            file.save()
        if local_storage.exists(file.file.name):
            file.is_on_local = True
            file.save()

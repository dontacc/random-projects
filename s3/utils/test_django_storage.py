import os
import django
import sys

a = sys.path.append('/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_authentication.settings')
django.setup()

from django.core.files.storage import storages, default_storage
from s3.models import File


def check_files():
    s3_storage = storages["default"]
    local_storage = storages["local"]
    files = File.objects.all()
    for file in files:
        if s3_storage.exists(file.file.name) is False:
            print(f"{file.file.url} does not exist")

    # return {
    #     "s3": s3_storage.exists(file.file.name),
    #     "local": local_storage.exists(file.file.name)
    # }





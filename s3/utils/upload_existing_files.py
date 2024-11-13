import os
import boto3
import django, sys
from django.conf import settings

sys.path.append('/Users/mac/Desktop/pingi_task/user_authentication/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_authentication.settings')
django.setup()


def upload_directory(directory_path, bucket_name):
    s3 = boto3.client(
        service_name='s3',
        endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )

    for root, dir, files in os.walk(directory_path):
        for file_name in files:
            file_path = f"./{directory_path}/{file_name}"
            objects_name = f"/{directory_path}/{file_name}"
            s3.upload_file(
                file_path,
                bucket_name,
                objects_name
            )


upload_directory('media', 'pingi-bucket')

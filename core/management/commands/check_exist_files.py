from django.core.management.base import BaseCommand
from django.core.management import call_command
from s3.tasks.check_exist_files import check_s3_and_local


class Command(BaseCommand):

    def handle(self, *args, **options):
        check_s3_and_local.delay()

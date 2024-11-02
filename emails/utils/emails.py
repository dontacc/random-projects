from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from time import sleep


class Email:

    @staticmethod
    @shared_task
    def send_email(subject, message):
        sleep(4)
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST,
            recipient_list=["pomib30805@regishub.com"]
        )

    @staticmethod
    def change_password_email():
        Email.send_email.delay(
            subject="Reset Password",
            message="this is reset password mail"
        )

        return None

from django.http import HttpResponse
from emails.utils import Email


def change_password(request):
    Email.change_password_email()
    return HttpResponse("email Sent")

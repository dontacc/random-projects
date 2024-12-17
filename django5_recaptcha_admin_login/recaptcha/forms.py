from django.contrib.admin.forms import (
    AdminAuthenticationForm as _AdminAuthenticationForm
)

from django5_recaptcha_admin_login.captcha.fields import ReCaptchaField


class AdminAuthenticationForm(_AdminAuthenticationForm):
    captcha = ReCaptchaField()

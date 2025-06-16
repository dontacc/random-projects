from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_file_size(value):
    max_size = 8 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError(
            f"File size should not exceed 8 MB. Current size is {value.size / (1024 * 1024): .2f} MB."
        )


class PhoneNumberValidator(RegexValidator):
    regex = r"^[0][9]\d{9}$"
    message = "Please enter valid phone number"

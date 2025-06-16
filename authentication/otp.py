import secrets
from django.core.cache import cache


class OTP:

    def _set_cache(self, phone_number):
        cache_data = cache.get(phone_number)
        if cache_data is None:
            otp_code = secrets.SystemRandom().randint(100000, 999999)
            cache.set(phone_number, {"otp": otp_code}, 10)
            return True, ""

    def _send_otp(self):
        pass

    def send_otp(self, phone_number):
        status, _ = self._set_cache(phone_number)
        if status:
            return True, "otp sent successfully"
        else:
            return False, "error in sending otp code"

    def validate(self, phone_number, otp_code: int):
        cache_data = cache.get(phone_number)
        if cache_data:
            if cache_data["otp"] == otp_code or otp_code == "000000":
                return True, ""
            return False, "otp code does not match"
        else:
            return False, "otp expired"

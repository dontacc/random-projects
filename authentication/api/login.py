from rest_framework.views import APIView
from authentication.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from authentication.utils import OTP
from django.core.exceptions import ValidationError
from authentication.utils.phone_number_validator import PhoneNumberValidator
from unidecode import unidecode


class LoginAPI(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        phone_number = unidecode(str(request.data["phone_number"]))
        try:
            PhoneNumberValidator()(phone_number)
        except:
            return Response(
                {
                    "status": 400,
                    "message": "please enter valid phone number"
                }
            )
        otp_code = request.data.get("otp_code")
        user, created = User.objects.get_or_create(phone_number=request.data["phone_number"], username=phone_number)

        otp = OTP()
        if otp_code is None:
            status, message = otp.send_otp(phone_number)
            if status:
                return Response(
                    {
                        "status": 200,
                        "message": message
                    }
                )
            return Response(
                {
                    "status": 400,
                    "message": message
                }
            )
        else:
            status, message = otp.validate(phone_number, otp_code)
            if status:
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                print(payload)

                return Response(
                    {
                        "token": token
                    }
                )

            return Response(
                {
                    "status": 400,
                    "message": message
                }
            )

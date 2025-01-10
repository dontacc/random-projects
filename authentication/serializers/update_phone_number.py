from rest_framework import serializers
from authentication.models import User


class UpdatePhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "phone_number",
            "username",
        ]
    # phone_number = serializers.CharField()
    # username = serializers.CharField()

    # def update(self, instance, validated_data):
    #     instance.phone_number = validated_data["phone_number"]
    #     instance.save()
    #
    #     return instance

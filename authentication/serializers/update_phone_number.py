from rest_framework import serializers
from authentication.models import User


class UpdatePhoneNumberSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = [
            "phone_number",
            "username",
        ]

    def validate(self, attrs):
        attrs["username"] = attrs["phone_number"]
        print(attrs)
        return attrs
    # phone_number = serializers.CharField()
    # username = serializers.CharField()

    # def update(self, instance, validated_data):
    #     instance.phone_number = validated_data["phone_number"]
    #     instance.save()
    #
    #     return instance

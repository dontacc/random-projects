from rest_framework import serializers
from authentication.models import User


class UpdatePhoneNumberSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = [
            "phone_number",
            "username",
        ]

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["phone_number"], phone_number=validated_data["phone_number"])
        return user
    # def validate(self, attrs):
    #     print(attrs)
    #     attrs["username"] = attrs["phone_number"]
    #     return attrs



    # phone_number = serializers.CharField()
    # username = serializers.CharField()

    # def update(self, instance, validated_data):
    #     instance.phone_number = validated_data["phone_number"]
    #     instance.save()
    #
    #     return instance

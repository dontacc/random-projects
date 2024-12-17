from rest_framework import serializers

from authentication import models


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = (
            "phone_number",
        )

    def validate(self, attrs):
        attrs["phone_number"] = "123123131132"
        return attrs

    def update(self, instance, validated_data):
        if instance.phone_number:
            instance.phone_number = validated_data["phone_number"]
        else:
            print("ssssss")

        return super().update(instance, validated_data)

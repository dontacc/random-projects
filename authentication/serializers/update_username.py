from rest_framework import serializers


class UpdateUsernameSerializer(serializers.Serializer):
    username = serializers.CharField()
    phone_number = serializers.CharField()
    first_name = serializers.CharField()

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

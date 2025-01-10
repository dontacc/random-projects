from rest_framework import serializers
from authentication.models import User


class ListDataSerializer(serializers.Serializer):
    # user_id = serializers.IntegerField(source="id")
    phone_number = serializers.CharField(max_length=15)

    # username = serializers.CharField(max_length=31)

    # def update(self, instance, validated_data):
    #     instance

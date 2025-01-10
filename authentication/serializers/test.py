from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=32)

from rest_framework import serializers
from authentication.models import User


class ListDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "phone_number",
            "status"
        ]

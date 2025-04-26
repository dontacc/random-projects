from rest_framework import serializers
from authentication.models import User


class ListDataSerializer(serializers.ModelSerializer):
    # user_id = serializers.IntegerField(source="id")

    class Meta:
        model = User
        fields = "__all__"

    # username = serializers.CharField(max_length=31)

    # def update(self, instance, validated_data):
    #     instance

from rest_framework import serializers
from authentication import models
from rest_framework.response import Response


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=31, required=False)

    def create(self, validated_data):
        print(self.context["request"].user)
        print(validated_data)
        return validated_data

    # def create(self, validated_data):
    #     if 1 == 1:
    #         return {"res": validated_data["username"]}
    #         raise serializers.ValidationError("saaaass")
    #     print(validated_data["username"])
    #     return {"token": validated_data["username"]}

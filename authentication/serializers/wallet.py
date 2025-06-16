from rest_framework import serializers
from authentication.models import *


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"


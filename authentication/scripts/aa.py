from rest_framework.views import APIView
from authentication.models import *
import random


def run():
    rates = [Rating(user_id=random.choice([1, 14]), rate_number=random.randint(0, 5)) for i in range(1000)]
    Rating.objects.bulk_create(rates)

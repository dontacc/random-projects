from django.urls import path
from sync_bnb.api import *

urlpatterns = [
    path("transaction-history/", TransactionHistory.as_view(), name="transaction-history"),
    path("bep-20-token/", GetBep20token.as_view(), name="get-bep-token")
]

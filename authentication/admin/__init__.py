from django.contrib import admin
from .user import UserAdmin

from authentication.models import User, Wallet

admin.site.register(User, UserAdmin)
admin.site.register(Wallet)

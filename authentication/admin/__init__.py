from django.contrib import admin
from .user import UserAdmin

from authentication.models import User, Wallet
from django.contrib.auth.models import Group
from .user import CustomGroupAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Wallet)
admin.site.unregister(Group)
admin.site.register(Group, CustomGroupAdmin)

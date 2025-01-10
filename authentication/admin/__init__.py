from django.contrib import admin
from django.contrib.auth.models import Group
from .user import CustomGroupAdmin
from .user import UserAdmin

from authentication.models import (
    User,
    Wallet,
    Author,
    Book,
)


admin.site.unregister(Group)

admin.site.register(User, UserAdmin)
admin.site.register(Wallet)
admin.site.register(Author)
admin.site.register(Book)

admin.site.register(Group, CustomGroupAdmin)

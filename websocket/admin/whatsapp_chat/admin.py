from django.contrib import admin


class ChatAdmin(admin.ModelAdmin):
    pass


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "is_online")
    list_display_links = ("id", "user")

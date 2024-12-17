from django import forms
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.forms import SelectMultiple


class CustomGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'permissions': SelectMultiple(attrs={
                'style': 'width: 500px; height: 400px;',
            })
        }


class CustomGroupAdmin(GroupAdmin):
    form = CustomGroupForm
    # filter_horizontal = ("permissions",)


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username")
    readonly_fields = ("password",)

    # fieldsets = [
    #     ("Personal", {"fields": ["username", "first_name"]})
    # ]

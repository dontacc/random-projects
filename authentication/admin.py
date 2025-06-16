from django import forms
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.forms import SelectMultiple

from django.contrib import admin
from authentication.models import *


class CustomGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'permissions': SelectMultiple(attrs={
                'style': 'width: 600px; height: 400px;',
            })
        }


class CustomGroupAdmin(GroupAdmin):
    form = CustomGroupForm
    # filter_horizontal = ("permissions",)


class WalletInline(admin.StackedInline):
    """
    StackedInline or TabularInline
    these classes is only use for ForeignKey or OneToOne fields
    """
    model = Wallet
    max_num = 1


class UserAdmin(admin.ModelAdmin):
    inlines = [WalletInline]
    list_display = ("id", "username")
    readonly_fields = ("password",)
    list_display_links = ("id", "username")

    # fieldsets = [
    #     ("Personal", {"fields": ["username", "first_name"]})
    # ]

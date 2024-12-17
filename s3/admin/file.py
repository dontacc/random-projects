from django.contrib import admin
from django.utils.html import mark_safe


class CustomFilterFile(admin.SimpleListFilter):
    title = "Exist files"
    parameter_name = "file"

    def lookups(self, request, model_admin):
        return (
            ("on_s3", "Is on S3"),
            ("on_local", "Is on Local"),
            ("not_on_s3", "Not exist on S3"),
            ("not_on_local", "Not exist on Local")
        )

    def queryset(self, request, queryset):
        if self.value() == "on_s3":
            return queryset.filter(is_on_s3=True)
        elif self.value() == "on_local":
            return queryset.filter(is_on_local=True)
        elif self.value() == "not_on_s3":
            return queryset.filter(is_on_s3=False)
        elif self.value() == "not_on_local":
            return queryset.filter(is_on_local=False)

        return queryset


class FileAdmin(admin.ModelAdmin):
    list_display = ("id", "show_file", "is_on_s3", "is_on_local")
    list_display_links = ("id", "show_file",)
    list_editable = ("is_on_s3", "is_on_local")
    list_filter = (CustomFilterFile,)

    def show_file(self, obj):
        return mark_safe('<img src="{}" style="max-width:140px;"/>'.format(obj.file.url))


class TestAdmin(admin.ModelAdmin):
    list_display = ("file",)

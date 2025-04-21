from django.contrib import admin

from .models import Push, ResponseStatus

# Register your models here.

admin.site.register(ResponseStatus)


@admin.register(Push)
class PushDumpAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "response_status_code",
        "created_at",
    )  # Columns in list view
    search_fields = ("content",)  # Searchable fields
    list_filter = ("created_at",)  # Sidebar filters
    ordering = ("-created_at",)  # Default order in admin
    readonly_fields = ("uuid_key", "created_at")  # Prevent edits to these

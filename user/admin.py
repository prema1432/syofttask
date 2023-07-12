from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

admin.site.site_title = "Syoft - Admin"
admin.site.site_header = "Syoft - Admin"
admin.site.index_title = "Syoft - Dashboard"


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role")
    list_filter = ("role",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Roles", {"fields": ("role",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "role"),
            },
        ),
    )
    date_hierarchy = "date_joined"


admin.site.register(User, CustomUserAdmin)

# app_users/admin.py

from typing import Any

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User  # Импортируем свою модель, не django.contrib.auth.models!


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Админ-панель для пользователей."""

    model = User
    ordering = ("email",)

    list_display = ("email", "is_active", "is_staff", "is_superuser", "date_joined")
    list_filter = ("is_active", "is_staff", "is_superuser", "date_joined")
    search_fields = ("email",)

    fieldsets: tuple[tuple[str | None, dict[str, Any]], ...] = (
        (None, {"fields": ("email", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets: tuple[tuple[str | None, dict[str, Any]], ...] = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

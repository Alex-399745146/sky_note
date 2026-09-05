# app_notes/admin.py
from django.contrib import admin

from app_notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    """Настройка отображения в административной панели."""

    list_display = (
        "id",
        "title",
        "owner",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
        "updated_at",
    )
    search_fields = (
        "title",
        "content",
        "owner__username",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    ordering = ("-created_at",)

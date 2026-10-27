# app_notes/models.py
from django.conf import settings
from django.db import models


class Note(models.Model):
    """Модель записи личного дневника."""

    title = models.CharField(
        max_length=200,
        verbose_name="Заглавие",
    )
    content = models.TextField(
        verbose_name="Фабула",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notes",
        verbose_name="Владелец",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата изменения",
    )

    class Meta:
        verbose_name = "Запись дневника"
        verbose_name_plural = "Записи дневника"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

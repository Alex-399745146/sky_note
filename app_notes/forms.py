from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """Форма создания/редактирования заметки."""

    class Meta:
        model = Note
        fields = ("title", "content")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control form-control-lg",
                    "placeholder": "Заголовок",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Фабула",
                    "rows": 12,
                }
            ),
        }

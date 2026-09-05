# app_users/forms.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """Форма регистрации нового пользователя."""

    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
        )
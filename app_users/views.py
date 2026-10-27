# app_users/views.py

from typing import Any

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import LoginForm, RegisterForm


@require_http_methods(["GET", "POST"])
def register_view(request: HttpRequest) -> HttpResponse:
    """Регистрация нового пользователя."""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("app_notes:note_list")
    else:
        form = RegisterForm()

    return render(request, "app_users/register.html", {"form": form})


@require_http_methods(["GET", "POST"])
def login_view(request: HttpRequest) -> HttpResponse:
    """Вход пользователя по email и паролю."""
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("app_notes:note_list")
    else:
        form = LoginForm()

    return render(request, "app_users/login.html", {"form": form})


@login_required
@require_http_methods(["GET", "POST"])
def logout_view(request: HttpRequest) -> HttpResponse:
    """Выход пользователя."""
    if request.method == "POST":
        from django.contrib.auth import logout

        logout(request)
        return redirect("app_users:login")

    return render(request, "app_users/logout.html")

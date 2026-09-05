# app_users/views.py

from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.shortcuts import redirect

from app_users.forms import RegisterForm


class UserLoginView(LoginView):
    """Представление входа пользователя."""

    template_name = "app_users/login.html"
    redirect_authenticated_user = True


def register(request):
    """Представление регистрации нового пользователя."""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("app_notes:note_list")
    else:
        form = RegisterForm()

    return render(
        request,
        "app_users/register.html",
        {"form": form},
    )


def user_logout(request):
    """Представление выхода пользователя."""
    logout(request)
    return redirect("app_users:login")
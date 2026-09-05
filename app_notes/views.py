# app_notes/views.py

from typing import Any

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import NoteForm
from .models import Note


class NoteListView(LoginRequiredMixin, ListView):
    """Список заметок пользователя."""

    model = Note
    template_name = "app_notes/note_list.html"
    context_object_name = "notes"

    def get_queryset(self):
        queryset = Note.objects.filter(owner=self.request.user).order_by("-created_at")

        search_query = self.request.GET.get("q", "")
        if search_query:
            queryset = queryset.filter(
                models.Q(title__icontains=search_query) | models.Q(content__icontains=search_query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("q", "")
        return context


class NoteDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """Просмотр отдельной записи."""

    model = Note
    template_name = "app_notes/note_detail.html"
    context_object_name = "note"

    def test_func(self):
        note = self.get_object()
        return note.owner == self.request.user


class NoteCreateView(LoginRequiredMixin, CreateView):
    """Создание новой записи."""

    model = Note
    form_class = NoteForm
    template_name = "app_notes/note_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, "Запись успешно создана.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("app_notes:note_list")


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Редактирование записи."""

    model = Note
    form_class = NoteForm
    template_name = "app_notes/note_form.html"

    def test_func(self):
        note = self.get_object()
        return note.owner == self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Запись успешно обновлена.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("app_notes:note_detail", kwargs={"pk": self.object.pk})


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Удаление записи."""

    model = Note
    template_name = "app_notes/note_confirm_delete.html"
    context_object_name = "note"

    def test_func(self):
        note = self.get_object()
        return note.owner == self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Запись успешно удалена.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("app_notes:note_list")

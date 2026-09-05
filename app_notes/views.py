# app_notes/views.py

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from app_notes.models import Note


class NoteListView(LoginRequiredMixin, ListView):
    """Список личных записей пользователя."""

    model = Note
    template_name = "app_notes/note_list.html"
    context_object_name = "notes"

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)


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
    template_name = "app_notes/note_form.html"
    fields = ("title", "content")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        # Сообщение добавляем только после успешного создания
        if self.object:
            messages.success(request, "Запись успешно создана.")
        return response

    def get_success_url(self):
        return reverse_lazy("app_notes:note_list")


class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Редактирование записи."""

    model = Note
    template_name = "app_notes/note_form.html"
    fields = ("title", "content")

    def test_func(self):
        note = self.get_object()
        return note.owner == self.request.user

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if hasattr(self, "object") and self.object:
            messages.success(request, "Запись успешно обновлена.")
        return response

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

    def post(self, request, *args, **kwargs):
        messages.success(request, "Запись успешно удалена.")
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy("app_notes:note_list")


class NoteSearchView(LoginRequiredMixin, ListView):
    """Поиск по личным записям пользователя."""

    model = Note
    template_name = "app_notes/search_results.html"
    context_object_name = "notes"

    def get_queryset(self):
        query = self.request.GET.get("q", "").strip()

        queryset = Note.objects.filter(owner=self.request.user)

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
                | Q(content__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "").strip()
        return context
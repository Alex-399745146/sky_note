from django.urls import path

from app_notes import views

app_name = "app_notes"

urlpatterns = [
    path("", views.NoteListView.as_view(), name="note_list"),
    path("create/", views.NoteCreateView.as_view(), name="note_create"),
    path("<int:pk>/", views.NoteDetailView.as_view(), name="note_detail"),
    path("<int:pk>/update/", views.NoteUpdateView.as_view(), name="note_update"),
    path("<int:pk>/delete/", views.NoteDeleteView.as_view(), name="note_delete"),
    path("search/", views.NoteSearchView.as_view(), name="note_search"),
]

from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("app_users.urls", namespace="app_users")),
    path("notes/", include("app_notes.urls", namespace="app_notes")),
    path("", RedirectView.as_view(url="/notes/", permanent=False)),
]

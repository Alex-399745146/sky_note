from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("app_users.urls", namespace="app_users")),
    path("", include("app_notes.urls", namespace="app_notes")),



]

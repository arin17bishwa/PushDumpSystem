# urls.py
from django.urls import path

from .views import store_push, json_pushes_view

urlpatterns = [
    path("push/json/", store_push),
    path("view/", json_pushes_view, name="json_viewer"),
]

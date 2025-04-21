# urls.py
from django.urls import path
from .views import store_push

urlpatterns = [
    path('push/json/', store_push),
]

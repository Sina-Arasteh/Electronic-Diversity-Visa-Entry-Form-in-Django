from django.urls import path
from . import views

urlpatterns = [
    path("", views.begin_entry),
    path("application", views.application , name="application")
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.begin_entry.as_view()),
    path("application", views.application.as_view() , name="application")
]

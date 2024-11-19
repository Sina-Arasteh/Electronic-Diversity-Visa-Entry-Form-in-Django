from django.urls import path
from . import views

urlpatterns = [
    path('', views.begin_entry),
    path('entry-form', views.entry_form , name="entry_form")
]

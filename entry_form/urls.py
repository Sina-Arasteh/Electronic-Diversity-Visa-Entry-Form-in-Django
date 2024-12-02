from django.urls import path
from . import views

app_name = "datefield"
urlpatterns = [
    path('', views.begin_entry),
    path('entry-form', views.entry_form , name="entry_form")
]

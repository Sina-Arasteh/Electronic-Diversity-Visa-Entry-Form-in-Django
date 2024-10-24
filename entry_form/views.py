from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ApplicationForm

# Create your views here.

class begin_entry(TemplateView):
    template_name = "entry_form/begin_entry.html"

class application(FormView):
    form_class = ApplicationForm
    template_name = "entry_form/application.html"



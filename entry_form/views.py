from django.shortcuts import render
from . import forms


def begin_entry(request):
    return render(request, 'entry_form/begin_entry.html')

def entry_form(request):
    if request.method == "POST":
        pass

    form = forms.EntrantForm()
    return render(request, "entry_form/entry_form.html", {
        "form": form,
    })    


from django import forms
from . import models

class EntrantForm(forms.ModelForm):
    month = forms.IntegerField(min_value=1, max_value=12)
    day = forms.IntegerField(min_value=1, max_value=31)
    year = forms.IntegerField(min_value=1907, max_value=2015)
    
    class Meta:
        model = models.Entrant
        fields = "__all__"
        widgets = {
            "gender": forms.RadioSelect,
            "education_level": forms.RadioSelect,
            "marital_status": forms.RadioSelect,
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(EntrantForm, self).__init__(*args, **kwargs)
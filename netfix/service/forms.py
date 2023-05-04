from django import forms
from django.forms import ModelForm
from .models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ['company_username']
        fields = ['name', 'description', 'field', 'price_per_hour']
        # widgets = {
        #     'company_username': forms.HiddenInput()
        # }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        if user.field_of_work != 'ALL_IN_ONE':
            del self.fields['field']

from django.forms import ModelForm
from .models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        exclude = ['company_username']
        fields = ['name', 'description', 'field', 'price_per_hour']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autofocus': 'autofocus'})
        # if the user field of work not ALL_IN_ONE, then company can add only
        # services of company field of work, so the no choice field available
        # and this field removed from the form
        if user.field_of_work != 'ALL_IN_ONE':
            del self.fields['field']

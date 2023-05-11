from django.forms import ModelForm

from base.models import ACTIVITY_CHOICES
from .models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        # the field company_username is excluded from the form, but present in the model Service
        exclude = ['company_username']
        fields = ['name', 'description', 'field', 'price_per_hour']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autofocus': 'autofocus'})
        # if the user field of work not ALL_IN_ONE, then company can add only
        # services of company field of work, so the no choice field available
        # and this field removed from the form

        # if user.field_of_work != 'ALL_IN_ONE':
        #     del self.fields['field']

        # wtf, these idiots from 01-edu in audit questions require
        # add the field of choice of one variant. Also they ban me on github
        # after i made review of their brown substance named "graphql",
        # in attempts to hide this shame from the readers.
        # So i cant make issues, and ... here is it, sniff it carefully

        if user.field_of_work != 'ALL_IN_ONE':
            self.fields['field'].choices = [
                (x, y) for x, y in ACTIVITY_CHOICES if x == user.field_of_work]

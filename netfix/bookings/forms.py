from django import forms

from bookings.models import Bookings


class BookingForm(forms.ModelForm):
    hours = forms.IntegerField(min_value=1)

    class Meta:
        model = Bookings
        fields = ['address', 'hours']

    def clean(self):
        cleaned_data = super().clean()
        hours = cleaned_data.get('hours')
        # if not hours:
        #     raise forms.ValidationError('Hours is required.')
        return cleaned_data

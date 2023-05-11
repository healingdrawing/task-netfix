from django import forms

from bookings.models import Bookings


class BookingForm(forms.ModelForm):
    hours = forms.IntegerField(min_value=1)

    class Meta:
        model = Bookings
        fields = ['address', 'hours']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget.attrs.update({'autofocus': 'autofocus'})

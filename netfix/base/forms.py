from django import forms
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from base.models import Kastrat


ACTIVITY_CHOICES_FORM = [
    ('ALL_IN_ONE', 'All in One'),
    ('AIR_CONDITIONER', 'Air Conditioner'),
    ('CARPENTRY', 'Carpentry'),
    ('ELECTRICITY', 'Electricity'),
    ('GARDENING', 'Gardening'),
    ('HOME_MACHINES', 'Home Machines'),
    ('HOUSEKEEPING', 'Housekeeping'),
    ('INTERIOR_DESIGN', 'Interior Design'),
    ('LOCKS', 'Locks'),
    ('PAINTING', 'Painting'),
    ('PLUMBING', 'Plumbing'),
    ('WATER_HEATERS', 'Water Heaters'),
]
"""have no CUSTOMER , ALL_IN_ONE used default"""


class CompanyCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    field_of_work = forms.ChoiceField(
        required=True, choices=ACTIVITY_CHOICES_FORM, initial='ALL_IN_ONE')

    class Meta:
        model = Kastrat
        fields = ('username', 'email', 'field_of_work',
                  'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': 'autofocus'})

    def clean_username(self):
        username = self.cleaned_data['username']
        if Kastrat.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if Kastrat.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use")
        return email

    def save(self, commit=True):
        company = super().save(commit=False)
        company.email = self.cleaned_data['email']
        company.field_of_work = self.cleaned_data['field_of_work']
        company.date_of_birth = timezone.now()
        if commit:
            company.save()
        return company


class CustomerCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(
        required=True, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Kastrat
        fields = ('username', 'email', 'date_of_birth',
                  'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': 'autofocus'})

    def clean_username(self):
        username = self.cleaned_data['username']
        if Kastrat.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if Kastrat.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use")
        return email

    def save(self, commit=True):
        customer = super().save(commit=False)
        customer.email = self.cleaned_data['email']
        customer.date_of_birth = self.cleaned_data['date_of_birth']
        if commit:
            customer.save()
        return customer


# make userloginform using email+ password instead of username + password
class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Kastrat
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'autofocus': 'autofocus'})

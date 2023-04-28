from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.db import transaction
from django.core.exceptions import ValidationError

from .models import User, Company, Customer


class DateInput(forms.DateInput):
    input_type = 'date'


def validate_email(value):
    # In case the email already exists in an email input in a registration form, this function is fired
    if User.objects.filter(email=value).exists():
        raise ValidationError(
            value + " is already taken.")


class CustomerSignUpForm(UserCreationForm):
    # add text placeholder to built-in field username
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Username'}))

    # add to UserCreationForm the field email, after built-in field username
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Email'}), validators=[validate_email])
    
    # add to UserCreationForm the field birth_date
    birth_date = forms.DateField(widget=DateInput)
    
    pass


class CompanySignUpForm(UserCreationForm):
    # add text placeholder to built-in field username
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Username'}))

    # add to UserCreationForm the field email, after built-in field username
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Email'}), validators=[validate_email])

   # add select widget to form field, with multiple choices
    field = forms.ChoiceField(widget=forms.Select, choices=(('Air Conditioner', 'Air Conditioner'),
                                                              ('All in One', 'All in One'),
                                                                ('Carpentry', 'Carpentry'),
                                                                ('Electricity',
                                                                'Electricity'),
                                                                ('Gardening', 'Gardening'),
                                                                ('Home Machines',
                                                                'Home Machines'),
                                                                ('House Keeping',
                                                                'House Keeping'),
                                                                ('Interior Design',
                                                                'Interior Design'),
                                                                ('Locks', 'Locks'),
                                                                ('Painting', 'Painting'),
                                                                ('Plumbing', 'Plumbing'),
                                                                ('Water Heaters', 'Water Heaters')), required=True)

                                                                

        

    pass


class UserLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Email'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['autocomplete'] = 'off'

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from base.models import Kastrat


class CustomerCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(
        required=True, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Kastrat
        fields = ('username', 'email', 'date_of_birth',
                  'password1', 'password2')

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

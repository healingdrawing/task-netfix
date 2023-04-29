from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomerCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(
        required=True, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'date_of_birth',
                  'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.date_of_birth = self.cleaned_data['date_of_birth']
        if commit:
            user.save()
        return user


# make userloginform using email+ password instead of username + password
class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

from django.contrib import messages
from django.forms import ValidationError
from django.shortcuts import render
from base.forms import CompanyCreationForm, CustomerCreationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from base.models import Kastrat

# Create your views here.


def home_view(request):
    return render(request, 'index.html')


def register_view(request):
    return render(request, 'register.html')


def register_customer(request):
    if request.method == 'POST':
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.email = user.email.lower()
            user.save()
            return render(request, 'login.html', {'form': UserLoginForm()})
    else:
        form = CustomerCreationForm()

    return render(request, 'register_customer.html', {'form': form})


def register_company(request):
    if request.method == 'POST':
        form = CompanyCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.email = user.email.lower()
            user.save()
            return render(request, 'login.html', {'form': UserLoginForm()})
    else:
        form = CompanyCreationForm()

    return render(request, 'register_company.html', {'form': form})


def login_view(request):
    form = UserLoginForm()
    if request.user.is_authenticated:
        return render(request, 'index.html')
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email'].lower()
            password = form.cleaned_data['password']
            try:
                if not Kastrat.objects.filter(email=email).exists():
                    raise ValidationError("email does not exist")
                user = Kastrat.objects.get(email=email)
                user = authenticate(request, email=email,
                                    password=password)
                if user is not None:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    form.add_error(None, "Invalid email or password")

            except:
                form.add_error(None, "email does not exist")
        else:
            form.add_error(None, "form is not valid")

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'index.html')

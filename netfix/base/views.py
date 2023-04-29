from django.contrib import messages
from django.shortcuts import render
from base.forms import CustomerCreationForm, UserLoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

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
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.save()
            # TODO: redirect to login page
            return render(request, 'index.html')
    else:
        form = CustomerCreationForm()

    return render(request, 'register_customer.html', {'form': form})


def register_company(request):
    return render(request, 'register_company.html')


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
                user = User.objects.get(email=email)
                user = authenticate(username=user.username,
                                    password=password)
                if user is not None:
                    login(request, user)
                    return render(request, 'index.html')
            except:
                messages.error(request, "Invalid email or password")
    return render(request, 'login.html', {'form': form})


# TODO: move services to separate app later


def services_view(request):
    return render(request, 'services.html')

from django.contrib import messages
from django.forms import ValidationError
from django.shortcuts import render
from base.forms import CustomerCreationForm, UserLoginForm
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
            # TODO: redirect to login page
            return render(request, 'login.html', {'form': UserLoginForm()})
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
        print(request.POST, request.POST['email'], request.POST['password'])
        form = UserLoginForm(request.POST)
        if form.is_valid():
            print("form is valid",
                  form.cleaned_data['email'], form.cleaned_data['password'])
            email = form.cleaned_data['email'].lower()
            password = form.cleaned_data['password']
            print("email", email, "password", password)
            try:
                if not Kastrat.objects.filter(email=email).exists():
                    raise ValidationError("email does not exist")
                user = Kastrat.objects.get(email=email)
                print("Kastrat user", user, "user.username", user.username)
                user = authenticate(request, email=email,  # TODO: check this shit, still fail, need fix username vs email if possible
                                    password=password)
                print("Kastrat user after authenticate", user)

                # TODO: remove later. replacer for authenticate which is fails with good credentials. Code bottom works at the moment
                # if user is not None and user.check_password(password):
                #     print("GOOD PASSWORD MANUAL CHECK")
                #     login(request, user)
                #     return render(request, 'index.html')
                # else:
                #     print("PASSWORD MANUAL CHECK FAILED")

                if user is not None:
                    # todo: remove print later
                    print("user is not None. TRY TO LOGIN")
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    print("user is None", user)
                    form.add_error(None, "Invalid email or password")

            except:
                # todo: change to invalid email or password later, to not give info about existing emails
                form.add_error(None, "email does not exist")
        else:
            # todo: remove prints later, or restyle them
            print("form is NOT valid")
            print("form.cleaned_data", form.cleaned_data)
            print("form.data", form.data)

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'index.html')

# TODO: move services to separate app later


def services_view(request):
    return render(request, 'services.html')

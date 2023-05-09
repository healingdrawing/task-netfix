from django.contrib import messages
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse
from base.forms import CompanyCreationForm, CustomerCreationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from base.models import Kastrat
from service.models import Service

# Create your views here.

FILTER_CHOICES = [
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
"""to generate links to filter services by field of work"""

FILTER_CHOICES_DICT = dict(FILTER_CHOICES)


def convert_one_choice_to_verbose_name(choice):
    """some not clear place. When customer will call, returns without changes,
    but at least it possible to use dict above in template, without recreate new dict"""
    return FILTER_CHOICES_DICT[choice] if choice in FILTER_CHOICES_DICT else choice


def convert_services_choices_to_verbose_names(services):
    """replace two fields values with data without underscores"""
    for service in services:
        service.field = FILTER_CHOICES_DICT[service.field]
        service.company_username.field_of_work = FILTER_CHOICES_DICT[
            service.company_username.field_of_work]
    return services


def convert_bookings_choices_to_verbose_names(bookings):
    """replace two fields values with data without underscores"""
    for booking in bookings:
        booking.service.field = FILTER_CHOICES_DICT[booking.service.field]
        booking.service.company_username.field_of_work = FILTER_CHOICES_DICT[
            booking.service.company_username.field_of_work]
    return bookings


def home_view(request, service_field='ALL_IN_ONE'):
    if service_field not in FILTER_CHOICES_DICT or service_field == 'ALL_IN_ONE':
        services = Service.objects.all().order_by('-created_date')
    else:
        services = Service.objects.filter(
            field=service_field).order_by('-created_date')
    convert_services_choices_to_verbose_names(services)
    context = {
        'user': request.user,  # to manage navbar.html properly
        'services': services,
        'field_verbose_dict': FILTER_CHOICES_DICT,
    }
    return render(request, 'home.html', context)


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
                    return redirect(reverse('home'))
                else:
                    form.add_error(None, "Invalid email or password")
            except:
                form.add_error(None, "email does not exist")
        else:
            form.add_error(None, "form is not valid")

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def register_customer(request):
    return render(request, 'register_customer.html')


def register_company(request):
    return render(request, 'register_company.html')

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from bookings.forms import BookingForm

# from bookings.forms import BookingForm
from service.models import Service
from .forms import ServiceForm


def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, user=request.user)
        if form.is_valid():
            service = form.save(commit=False)
            service.company_username = request.user
            if request.user.field_of_work != 'ALL_IN_ONE':
                service.field = request.user.field_of_work
            else:
                service.field = form.cleaned_data['field']
            service.save()
            return render(request, 'profile.html', {'user': request.user})
    else:
        form = ServiceForm(user=request.user)
    return render(request, 'add_service.html', {'form': form})


# just show service from database, check the method is post

def service_view(request, service_id):
    service = Service.objects.get(id=service_id)
    context = {'service': service}
    return render(request, 'one_service.html', context)


def service_list_view(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

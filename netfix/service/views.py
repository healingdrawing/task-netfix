from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from base.views import convert_services_choices_to_verbose_names
from service.models import Service
from .forms import ServiceForm
from django.db.models import Count, Max


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
            # no need send any data f.e. {'user': request.user, 'history': history}
            # because it calls profile view, instead of just rendering profile.html
            # but you can send data , like second argument of "redirect" in curve brackets(dict)
            return redirect(reverse('profile'))
    else:
        form = ServiceForm(user=request.user)
    return render(request, 'add_service.html', {'form': form})


def service_view(request, service_id):
    service = Service.objects.get(id=service_id)
    # facepalm, but i do not want implement a new method, for one call
    service = convert_services_choices_to_verbose_names([service])[0]
    context = {'service': service, 'user': request.user}
    return render(request, 'one_service.html', context)


def service_list_view(request):
    # list of services sorted by number of bookings, first the most popular.
    # For the same number of bookings, sorting by latest booking first.
    services = Service.objects.annotate(
        num_bookings=Count('bookings'),
        latest_booking_date=Max('bookings__booking_date')
    ).order_by('-num_bookings', '-latest_booking_date')
    convert_services_choices_to_verbose_names(services)
    return render(request, 'services.html', {'services': services})

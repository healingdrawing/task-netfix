from django.shortcuts import render
from base.models import Kastrat
from base.views import convert_bookings_choices_to_verbose_names, convert_services_choices_to_verbose_names, convert_one_choice_to_verbose_name

from bookings.models import Bookings
from service.models import Service

# Create your views here.


def profile(request):
    history = None
    if request.user.field_of_work == 'CUSTOMER':
        history = Bookings.objects.filter(
            user=request.user).order_by('-booking_date')
        convert_bookings_choices_to_verbose_names(history)
    else:
        history = Service.objects.filter(
            company_username=request.user).order_by('-created_date')
        convert_services_choices_to_verbose_names(history)
    request.user.field_of_work = convert_one_choice_to_verbose_name(
        request.user.field_of_work)
    context = {
        'user': request.user,
        'history': history,
    }
    return render(request, 'profile.html', context)


def public_profile(request, username):
    user = Kastrat.objects.get(username=username)
    user.field_of_work = convert_one_choice_to_verbose_name(user.field_of_work)
    history = None
    if user.field_of_work == 'CUSTOMER':
        # at the moment this never fires with normal site usage,
        # because only the company has links to a public profile
        # but for the emergency case, it can prevent potential issues
        history = Bookings.objects.filter(
            user=user).order_by('-booking_date')
    else:
        history = Service.objects.filter(
            company_username=user).order_by('-created_date')
        convert_services_choices_to_verbose_names(history)
    context = {
        # to manage navbar.html properly
        'user': request.user,
        # to show public user's profile, and choose history section of template
        'public_user': user,
        'history': history,
    }
    return render(request, 'public_profile.html', context)

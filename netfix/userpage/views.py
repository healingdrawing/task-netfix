from django.shortcuts import render
from base.models import Kastrat

from bookings.models import Bookings
from service.models import Service

# Create your views here.


def profile(request):
    history = None
    if request.user.field_of_work == 'CUSTOMER':
        history = Bookings.objects.filter(
            user=request.user).order_by('-booking_date')
    else:
        history = Service.objects.filter(
            company_username=request.user).order_by('-created_date')
    context = {
        'user': request.user,
        'history': history,
    }
    return render(request, 'profile.html', context)


def public_profile(request, username):
    user = Kastrat.objects.get(username=username)
    history = None
    if user.field_of_work == 'CUSTOMER':
        history = Bookings.objects.filter(
            user=user).order_by('-booking_date')
    else:
        history = Service.objects.filter(
            company_username=user).order_by('-created_date')
    context = {
        # to manage navbar.html properly
        'user': request.user,
        # to show public user's profile, and choose history section of template
        'public_user': user,
        'history': history,
    }
    return render(request, 'public_profile.html', context)

from django.shortcuts import render

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

from decimal import Decimal
from django.shortcuts import redirect, render

# Create your views here.


from django.shortcuts import render
from django.urls import reverse
from bookings.models import Bookings

from service.models import Service
from .forms import BookingForm


def booking_view(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.method == 'POST':
        booking = Bookings(service=service, user=request.user)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # or however you're setting the user
            booking.price = service.price_per_hour * int(request.POST['hours'])
            booking.save()
            # no need send any data f.e. {'user': request.user, 'history': history}
            # because it calls profile view, instead of just rendering profile.html
            # but you can send data , like second redirect argument in curve brackets
            return redirect(reverse('profile'))
    else:
        form = BookingForm(instance=Bookings(service=service))
    return render(request, 'book_service.html', {'form': form, 'service': service})

from decimal import Decimal
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
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
            # todo: also need generate list of bookings later, because redirect loosing data
            return render(request, 'profile.html', {'user': request.user})
    else:
        form = BookingForm(instance=Bookings(service=service))
    return render(request, 'book_service.html', {'form': form, 'service': service})

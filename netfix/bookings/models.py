from django.db import models


# Create your models here.
from django.forms import ValidationError
from base.models import Kastrat
from service.models import Service
from datetime import datetime


class Bookings(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(Kastrat, on_delete=models.CASCADE)
    address = models.TextField(null=False)
    booking_date = models.DateTimeField(default=datetime.now, null=False)
    price = models.DecimalField(
        max_digits=8, decimal_places=2)  # service.price_per_hour * hours

    def __str__(self):
        # according to the task these are the fields that must be displayed in services list
        return f"{self.service.name} - {self.service.field} - {self.price} - {self.booking_date}"

    def clean(self):
        if self.user.field_of_work != 'CUSTOMER':
            raise ValidationError('Only customer can book service')
        self.address = self.address.strip()  # Trim leading and trailing whitespace
        if not self.address:
            raise ValidationError('Address is required')

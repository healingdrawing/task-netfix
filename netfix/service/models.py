from django.db import models

from base.models import ACTIVITY_CHOICES, Kastrat

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    field = models.CharField(
        max_length=50,
        choices=[
            (x, y) for x, y in ACTIVITY_CHOICES if x not in ['ALL_IN_ONE', 'CUSTOMER']
        ]
    )
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    company_username = models.ForeignKey(
        Kastrat, on_delete=models.CASCADE, to_field='username', limit_choices_to={'field_of_work__ne': 'CUSTOMER'})

    def __str__(self):
        return self.name

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.


ACTIVITY_CHOICES = [
    ('CUSTOMER', 'Customer'),
    ('AIR_CONDITIONER', 'Air Conditioner'),
    ('ALL_IN_ONE', 'All in One'),
    ('CARPENTRY', 'Carpentry'),
    ('ELECTRICITY', 'Electricity'),
    ('GARDENING', 'Gardening'),
    ('HOME_MACHINES', 'Home Machines'),
    ('HOUSEKEEPING', 'Housekeeping'),
    ('INTERIOR_DESIGN', 'Interior Design'),
    ('LOCKS', 'Locks'),
    ('PAINTING', 'Painting'),
    ('PLUMBING', 'Plumbing'),
    ('WATER_HEATERS', 'Water Heaters'),
]
"""CUSTOMER used default, and means it is not a company, just to use one "user" implementation"""


class Kastrat(AbstractUser):
    """extended AbstractUser with removed two fields (groups, user_permissions)"""
    # remove two fields "groups" and "user_permissions" from AbstractUser.
    # If do not do this, then conflict will be raised, and to solve it
    # need to provide complex solution, in same time these fields are not used
    groups = None
    user_permissions = None
    username = models.CharField(max_length=254, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    field_of_work = models.CharField(
        max_length=50, choices=ACTIVITY_CHOICES, default='CUSTOMER')
    # null=False means the field is required, blank=False means the field is required in forms
    date_of_birth = models.DateField(
        null=False, blank=False, default=timezone.now)

    # set the field "email" as unique identifier. Will be used for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = 'base'

    def __str__(self):
        return self.email

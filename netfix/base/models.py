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
"""CUSTOMER used default, and means it is not a company, just to use one user implementation"""


class Kastrat(AbstractUser):
    """extended AbstractUser with removed two fields (groups, user_permissions)"""
    groups = None
    user_permissions = None
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    field_of_work = models.CharField(
        max_length=50, choices=ACTIVITY_CHOICES, default='CUSTOMER')
    date_of_birth = models.DateField(
        null=False, blank=False, default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = 'base'

    def __str__(self):
        return self.email

# need prevent conflict with django.contrib.auth.models.User, it works but names of fields are not the same. And i do not need this functionality at the moment. So version above just remove conflicting fields groups and user_permissions. Also the name may be changed to CustomUser, to not harm the original User model, used by admin panel.
# class User(AbstractUser):
#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(max_length=254, unique=True)
#     date_of_birth = models.DateField(null=False, blank=False)

#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='user_groups',
#         blank=True,
#         verbose_name='groups',
#         help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='user_permissions',
#         blank=True,
#         verbose_name='user permissions',
#         help_text='Specific permissions for this user.',
#     )

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     class Meta:
#         app_label = 'base'

#     def __str__(self):
#         return self.email

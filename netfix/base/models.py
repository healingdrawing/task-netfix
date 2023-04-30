from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Kastrat(AbstractUser):
    """extended AbstractUser with removed two fields (groups, user_permissions)"""
    groups = None
    user_permissions = None
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    date_of_birth = models.DateField(null=False, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = 'base'

    def __str__(self):
        return self.email

# need prevent conflict with django.contrib.auth.models.User, it works but names of fields are not the same. And i do not need this functionality at the moment. So version above just remove conflicting fields groups and user_permissions. Also the name was changed to CustomUser, to not harm the original User model, used by admin panel.
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

# task-netfix

01-edu bull shit from "professionals". And you need to ... complete it

## description

https://github.com/01-edu/public/tree/master/subjects/netfix

After some manipulations, project template from "professionals" became able to show some pages.  
Few hours later was decided to drop this shit into the trash, and recreate project, because of:

- masterpiece design based eye bleeding (red/yellow/gray palette, the hammer and spanner on logo for web application with "painting" or "gardening" services)
- usage of three classes(the built-in `User`, and two extended) to manage users, when it enough to use just one extended from `AbstractUser` (admin is not required, so it also the reason to cut some not safe methods)
- synthetically generated "errors", which can happens naturally only under the heavy drugs, which also can raise some thinks 🤔

Look at this 01-edu masterpiece, carefully... this is full code of file from not completed project they provide to clients. The hardcoded list of choices(tuple of tuples) is just a full success.

```python

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    email = models.CharField(max_length=100, unique=True)


class Customer(models.Model):
    pass


class Company(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    field = models.CharField(max_length=70, choices=(('Air Conditioner', 'Air Conditioner'),
                                                     ('All in One', 'All in One'),
                                                     ('Carpentry', 'Carpentry'),
                                                     ('Electricity',
                                                      'Electricity'),
                                                     ('Gardening', 'Gardening'),
                                                     ('Home Machines',
                                                      'Home Machines'),
                                                     ('House Keeping',
                                                      'House Keeping'),
                                                     ('Interior Design',
                                                      'Interior Design'),
                                                     ('Locks', 'Locks'),
                                                     ('Painting', 'Painting'),
                                                     ('Plumbing', 'Plumbing'),
                                                     ('Water Heaters', 'Water Heaters')), blank=False, null=False)
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(0)], default=0)

    def __str__(self):
        return str(self.user.id) + ' - ' + self.user.username

```

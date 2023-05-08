from . import views
from django.urls import path

urlpatterns = [
    path('', views.profile, name='profile'),
    path('<str:username>', views.public_profile, name='public_profile'),
]

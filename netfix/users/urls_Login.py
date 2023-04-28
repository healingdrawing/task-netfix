from django.urls import path
from django.contrib.auth import views

from . import views as v

urlpatterns = [
    path('', v.UserLoginView.as_view(), name='login_user'),
]

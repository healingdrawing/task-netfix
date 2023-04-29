from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('register_customer/', views.register_customer, name="register_customer"),
    path('register_company/', views.register_company, name="register_company"),
]

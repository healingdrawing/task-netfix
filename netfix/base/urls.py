from . import views
from django.urls import path


urlpatterns = [
    path('', views.home_view, name="home"),
    path('filter/<str:service_field>/', views.home_view, name="home_with_filter"),
    path('register/', views.register_view, name="register"),
    path('register_customer/', views.register_customer, name="register_customer"),
    path('register_company/', views.register_company, name="register_company"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]

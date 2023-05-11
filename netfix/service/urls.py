from . import views
from django.urls import path

urlpatterns = [
    path('create', views.add_service, name='add_service'),
    path('', views.service_list_view, name="services"),
    path('<int:service_id>', views.service_view, name="one_service"),
]

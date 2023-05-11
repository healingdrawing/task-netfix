from django.urls import path

from . import views

urlpatterns = [
    path('book_service/<int:service_id>/',
         views.booking_view, name='book_service'),
]

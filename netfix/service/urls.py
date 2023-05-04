from . import views
from django.urls import path

urlpatterns = [
    path('create', views.add_service, name='add_service'),
    path('book', views.book_service, name='book_service'),

]

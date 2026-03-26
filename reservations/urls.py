from django.urls import path
from . import views

urlpatterns = [
    path('getListOfHotels', views.get_list_of_hotels, name='get_list_of_hotels'),
    path('reservationConfirmation', views.reservation_confirmation, name='reservation_confirmation'),
]

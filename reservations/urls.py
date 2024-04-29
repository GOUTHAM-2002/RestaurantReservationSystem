
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.reservations_create,name="reservation-create"),
    path("<int:reservation_id>/update/",views.reservation_update,name="reservation-update"),
    path("success/",views.reservation_seccess,name="reservation-success")
]
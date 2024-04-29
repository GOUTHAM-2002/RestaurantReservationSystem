from django.shortcuts import render,redirect
from .forms import ReservationForm
from .models import Reservations


def reservations_create(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reservation-success")
    else:
        form = ReservationForm()
    return render(request,"reservations/reservation_create.html",{"form":form})

def reservation_update(request,reservation_id):
    reservation = Reservations.objects.get(pk=reservation_id)
    if request.method == "POST":
        form = ReservationForm(request.POST,instance=reservation)
        if form.is_valid():
            form.save()
            return redirect("reservation-success")
    else:
        form = ReservationForm(instance=reservation)
    return render(request,"reservations/reservation_update.html",{"form":form})

def reservation_seccess(request):
    return render(request,"reservations/success.html")

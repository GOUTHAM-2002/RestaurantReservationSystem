from django import forms

from .models import Reservations

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservations
        fields = ["customer","restaurant","date","time","num_guests"]
from django import forms
from django.db import models
from .models import Client, Business, Reservation

class ReservationForm(forms.Form):
    name = forms.CharField(label='Nombre'))
    number_of_people=forms.IntegerField(label = "Numero de personas")
    table = forms.IntegerField(label = "Mesa") 
    reservation_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M', attrs={
                                       'placeholder': 'Ej: 15:35', 'type': 'time'}), label='Hora ')
    details=forms.CharField(label = 'Detalles')

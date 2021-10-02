from django.shortcuts import render
from .forms import ReservationForm
# Create your views here.

def reservation_form (request):
    if request.method == 'POST':
        form = ReservationForm()

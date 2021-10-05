from collections import _OrderedDictKeysView, namedtuple
from django.shortcuts import render
from .forms import ReservationForm
from .models import *

def reservation_form (request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            number_of_people = form.cleaned_data['number_of_people']
            table = form.cleaned_data['table']
            reservation_time = form.cleaned_data['reservation_time']
            details = form.cleaned_data['details']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            
            business = Business.objects.last()
            client = Client.objects.get_or_create(name=name, mobile_phone=phone, email=email)[0]
            reservation = Reservation.objects.create(client=client, business=business, number_of_people=number_of_people,
                                                     table=table, reservation_time=reservation_time, details=details, state='Confirmada')

            reservation.save()
            return render(request, 'app1/succes.html')


    return render(request, 'app1/reservation_form.html', {'form':form})

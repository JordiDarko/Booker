from django.db import models

STATE_CHOICE = [
    ('Confirmada', 'Confirmada'),
    ('Pendiente', 'Pendiente'),
    ('Cancelada', 'Cancelada'),
]

class Client (models.Model):
    name = models.CharField(max_length=500, verbose_name=(
        'Nombre'), null=True, blank=True)
    mobile_phone = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)


class Business (models.Model):
    name = models.CharField(max_length=500, verbose_name=(
        'Nombre'), null=True, blank=True)
    mobile_phone = models.CharField(max_length=500, null=True, blank=True)

class Reservation (models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True,)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    number_of_people = models.IntegerField(
        null=True, blank=True, default=0,  verbose_name='Numero de personas')
    table = models.IntegerField(
        null=True, blank=True, default=0,  verbose_name='Mesa')
    reservation_time = models.DateTimeField(
        auto_now_add=True, verbose_name=('Fecha y hora reserva'))
    state = models.CharField(
        max_length=100, choices=STATE_CHOICE, default='agua', verbose_name=('Estado'))
    details = models.CharField(max_length=500, null=True, blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=('Created at'))
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=('Last updated at'))
    


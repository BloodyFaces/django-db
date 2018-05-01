from django.contrib import admin
from flights.models import *


class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city')
    search_fields = ['name', 'country', 'city']

class PlaneAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_sits')
    search_fields = ['name']

class ClientAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    list_display = ('name', 'surname', 'gender', 'phone_number', 'email')
    search_fields = ['name', 'surname', 'gender']

class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'duration', 'date', 'departure', 'destination', 'plane')
    search_fields = ['id', 'duration', 'date', 'departure', 'destination']

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'sit_class', 'flight', 'client', 'cost', 'cost_currency')
    search_fields = ['id', 'sit_class', 'flight', 'client', 'cost']

# Register your models here.
admin.site.register(Airport, AirportAdmin)
admin.site.register(Plane, PlaneAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Ticket, TicketAdmin)
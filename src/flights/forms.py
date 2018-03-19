from django import forms
from flights.models import Ticket, Airport

SIT_CHOICES = (('economy', 'Economy'), ('business', 'Business'), )
YEARS = ('2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025')

class TicketForm(forms.Form):
    departure = forms.CharField(max_length=128)
    destination = forms.CharField(max_length=128)
    date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    sit_class = forms.CharField(max_length=32, widget=forms.Select(choices=SIT_CHOICES))
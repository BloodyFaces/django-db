from django import forms
from flights.models import Ticket

SIT_CHOICES = (('business', 'economy'), ('economy', 'business'),)

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ('client', )

        widgets = {
            'sit_class': forms.Select(choices=SIT_CHOICES),
        }
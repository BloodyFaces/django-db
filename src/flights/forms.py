from django import forms
from flights.models import Ticket, Airport, Client
from datetimewidget.widgets import DateTimeWidget

SIT_CHOICES = (('economy', 'Economy'), ('business', 'Business'), )
YEARS = ('2018', '2019')
GENDER = (('male', 'Male'), ('female', 'Female'))


class TicketForm(forms.Form):
    departure = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'From'}), label='')
    destination = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'To'}), label='')
    date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS), label='')
    sit_class = forms.CharField(max_length=32, widget=forms.Select(choices=SIT_CHOICES), label='')

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'gender', 'phone_number', 'email']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}),
            'gender': forms.Select(choices=GENDER),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

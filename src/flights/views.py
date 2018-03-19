from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from flights.forms import TicketForm
from flights.models import Ticket


# Create your views here.
class FlightsTemplateView(View):
    template_name = 'home.html'

    def get(self, request):
        form = TicketForm(request.POST or None)
        return render(request, 'home.html', {'form': form})

class TicketListView(ListView):
    model = Ticket
    template_name = 'tickets.html'

    def get_queryset(self):
        form = TicketForm(request.GET or None)
        print()
        return Ticket.objects.filter
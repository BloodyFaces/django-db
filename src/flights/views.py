from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.db.models import Q
from datetime import date
from flights.forms import TicketForm
from flights.models import Ticket, Flight


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
        dep = self.request.GET.get('departure')
        des = self.request.GET.get('destination')
        date_month = self.request.GET.get('date_month')
        date_day = self.request.GET.get('date_day')
        date_year = self.request.GET.get('date_year')
        sit_class = self.request.GET.get('sit_class')
        sit_class = sit_class.capitalize()
        fdate = date(year=int(date_year), month=int(date_month), day=int(date_day))
        flights = Flight.objects.filter(
            Q(date=fdate) |
            Q(departure__city=dep) |
            Q(destination__city=des)
            )
        if flights is None:
            query = None
        else:
            query = Ticket.objects.filter(flight__in=flights)
            query = query.filter(sit_class=sit_class)
        return query
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, DetailView
from django.urls import reverse
from django.db.models import Q
from datetime import date
from flights.forms import TicketForm, ClientForm
from flights.models import Ticket, Flight, Client, Airport


# Create your views here.
class FlightsTemplateView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = TicketForm()
        context = {'form': form}
        thanks = request.GET.get('thanks')
        if thanks:
            context['thanks'] = thanks
        return render(request, 'home.html', context)

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
        depar = Airport.objects.filter(city=dep).first()
        desti = Airport.objects.filter(city=des).first()
        flights = Flight.objects.filter(date=fdate)
        flights = flights.filter(departure=depar)
        flights = flights.filter(destination=desti)
        if flights is None:
            query = None
        else:
            query = Ticket.objects.filter(flight__in=flights)
            query = query.filter(sit_class=sit_class)
            query = query.filter(client__isnull=True)
        return query


class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'client_create.html'

    def get(self, request, *args, **kwargs):
        form = ClientForm(request.POST or None)
        if form.is_valid():
            pk = request.GET.get('pk')
            print("PK: ", pk)
            ticket = get_object_or_404(Ticket, pk=pk)
            return redirect('home')
        return render(request, 'client_create.html', {'form': form})


def create_client(request, pk=None):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        print("PK: ", pk)
        ticket = get_object_or_404(Ticket, pk=pk)
        client = form.save()
        ticket.client = client
        ticket.save()
        request.GET._mutable = True
        request.GET['thanks'] = 'Thanks for buying ticket in our service!'
        return redirect('home')
    return render(request, 'client_create.html', {'form': form})
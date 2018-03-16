from django.shortcuts import render, redirect
from django.views.generic import View
from flights.forms import TicketForm


# Create your views here.
class FlightsTemplateView(View):
    template_name = 'home.html'

    def get(self, request):
        form = TicketForm(request.POST or None)
        return render(request, 'home.html', {'form': form})
from django.urls import path
from .views import FlightsTemplateView, TicketListView

urlpatterns = [
    path('', FlightsTemplateView.as_view(), name='home'),
    path('tickets', TicketListView.as_view(), name='tickets'),
]
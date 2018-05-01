from django.urls import path
from .views import FlightsTemplateView, TicketListView, TicketDetailView, create_client

urlpatterns = [
    path('', FlightsTemplateView.as_view(), name='home'),
    path('tickets/', TicketListView.as_view(), name='tickets'),
    path('tickets/<int:pk>/', create_client, name='client'),
]
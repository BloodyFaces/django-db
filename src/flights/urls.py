from django.urls import path
from .views import FlightsTemplateView

urlpatterns = [
    path('', FlightsTemplateView.as_view(), name='home'),
]
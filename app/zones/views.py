from django.views.generic import ListView, DetailView, UpdateView

from .models import Agency, Zone


class ZoneListView(ListView):
    model = Zone
    
class ZoneDetailView(DetailView):
    model = Zone
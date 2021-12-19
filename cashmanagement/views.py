from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from cashmanagement.models import Inflow

# Create your views here.
class InflowListView(ListView):
    model = Inflow
    paginate_by = 100


class InflowCreateView(CreateView):
    model = Inflow
    fields = ['amount', 'date', 'type', 'repetitive',
              'repetition_interval', 'repetition_time', 'created_at']


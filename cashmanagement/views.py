from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from rest_framework import viewsets
from .serializers import AccountSerializer
from .models import Account

from cashmanagement.models import Inflow


# Create your views here.
class InflowListView(ListView):
    model = Inflow
    paginate_by = 100


class InflowCreateView(CreateView):
    model = Inflow
    fields = ['amount', 'date', 'type', 'repetitive',
              'repetition_interval', 'repetition_time']
    success_url = reverse_lazy('cashmanagement:inflow_list')


class AccountView(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


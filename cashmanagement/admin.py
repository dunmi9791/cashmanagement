from django.contrib import admin
from cashmanagement.models import Inflow, Outflow, Balance

# Register your models here.
admin.site.register(Inflow)
admin.site.register(Outflow)
admin.site.register(Balance)

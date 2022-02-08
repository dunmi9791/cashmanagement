from django.contrib import admin
from cashmanagement.models import Inflow, Outflow, Balance, Transaction, Category, Account

# Register your models here.
admin.site.register(Inflow)
admin.site.register(Outflow)
admin.site.register(Balance)
admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Transaction)

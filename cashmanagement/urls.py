from django.urls import path

from cashmanagement import views


app_name = 'cashmanagement'

urlpatterns = [
    path('inflow_list/', views.InflowListView.as_view(), name='inflow_list'),
    path('inflow_create/', views.InflowCreateView.as_view(), name='inflow_create')
]
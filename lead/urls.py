from django.urls import path
from . import views

urlpatterns = [
    path('', views.leads_list, name='leads_list'),
    path('new-lead/', views.new_lead, name='new_lead'),
]
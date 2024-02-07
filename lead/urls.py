from django.urls import path
from . import views

urlpatterns = [
    path('new-lead/', views.new_lead, name='new_lead'),
]
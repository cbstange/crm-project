from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def new_lead(request):
    return render(request, 'new_lead.html')

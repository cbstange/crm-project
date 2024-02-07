from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

# User cannot access dashboard unless they are logged in
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
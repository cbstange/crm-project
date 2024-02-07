from django.shortcuts import render

# Create your views here.

def dashboard(reqeust):
    return render(request, 'dashboard.html')
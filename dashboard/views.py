from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from lead.models import Lead
from client.models import Client
from team.models import Team

# User cannot access dashboard unless they are logged in
@login_required
def dashboard(request):
    
    
    team = Team.objects.filter(created_by=request.user)
    if team:
        team = team[0]
    else:
        team = None


    
    leads = Lead.objects.filter(team=team, converted_to_client=False).order_by('-created_on')[0:5]
    clients = Client.objects.filter(team=team).order_by('-created_on')[0:5]

    return render(request, 'dashboard.html', {
        'leads': leads,
        'clients': clients,
    })
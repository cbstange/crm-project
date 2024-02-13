from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .forms import NewLeadForm
from .models import Lead
from client.models import Client
from team.models import Team

# Display leads as a list
@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user, converted_to_client=False)

    return render(request, 'leads_list.html', {
        'leads': leads
    })


# Display lead details
@login_required
def leads_detail(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    return render(request, 'leads_detail.html', {
        'lead': lead
    })


# Delete a lead with message confirmation
@login_required
def leads_delete(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()

    messages.success(request, 'Lead successfully deleted.')

    return redirect('leads_list')


# Edit a lead
@login_required
def leads_edit(request,pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    
    if request.method == 'POST':
        form = NewLeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()

            messages.success(request, 'Lead successfully edited.')

            return redirect('leads_list')
    else:
        form = NewLeadForm(instance=lead)

    return render(request, 'leads_edit.html', {
        'form': form
    })


# Add a new lead - form submition
@login_required
def new_lead(request):
    if request.method == 'POST':
        form = NewLeadForm(request.POST)

        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.team = team
            lead.save()

            messages.success(request, 'Lead successfully created.')

            return redirect('leads_list')
    else:
        form = NewLeadForm()

    return render(request, 'new_lead.html', {
        'form': form
    })


# Convert a lead to a client
@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    team = Team.objects.filter(created_by=request.user)[0]

    client = Client.objects.create(
        name=lead.name,
        email=lead.email,
        description=lead.description,
        created_by=request.user,
        team=team,
    )

    lead.converted_to_client = True
    lead.save()

    messages.success(request, 'Lead converted to a client.')

    return redirect('leads_list')

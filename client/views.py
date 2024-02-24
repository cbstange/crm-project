from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Client
from .forms import NewClientForm
from team.models import Team

# Display a list of clients
@login_required
def clients_list(request):
    clients = Client.objects.filter(created_by=request.user)

    return render(request, 'clients_list.html', {
        'clients': clients
    })

# Display client details
@login_required
def clients_detail(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)

    return render(request, 'clients_detail.html', {
        'client': client
    })

# Create a new client
@login_required
def new_client(request):
    if request.method == 'POST':
        form = NewClientForm(request.POST)

        if form.is_valid():
            team = Team.objects.filter(created_by=request.user)[0]

            client = form.save(commit=False)
            client.created_by = request.user
            client.team = team
            client.save()

            messages.success(request, 'Client successfully created.')

            return redirect('clients_list')
    else:
        form = NewClientForm()

    return render(request, 'new_client.html', {
        'form': form
    })

# Delete a client
@login_required
def clients_delete(request, pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    client.delete()

    messages.success(request, 'Client successfully deleted.')

    return redirect('clients_list')

# Edit a client
@login_required
def clients_edit(request,pk):
    client = get_object_or_404(Client, created_by=request.user, pk=pk)
    
    if request.method == 'POST':
        form = NewClientForm(request.POST, instance=client)

        if form.is_valid():
            form.save()

            messages.success(request, 'Client successfully edited.')

            return redirect('clients_list')
    else:
        form = NewClientForm(instance=client)

    return render(request, 'clients_edit.html', {
        'form': form
    })
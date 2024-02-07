from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import NewLeadForm
from .models import Lead

@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user)

    return render(request, 'leads_list.html', {
        'leads': leads
    })


@login_required
def new_lead(request):
    if request.method == 'POST':
        form = NewLeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()

            return redirect('dashboard')
    else:
        form = NewLeadForm()   
    return render(request, 'new_lead.html', {
        'form': form
    })

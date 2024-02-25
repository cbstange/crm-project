from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Userprofile
from team.models import Team
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Create a UserProfile instance for the newly created user
            Userprofile.objects.create(user=user)

            # Check if the user is authenticated before creating a team
            if request.user.is_authenticated:
                team = Team.objects.create(name='The team name', created_by=request.user)

                # Add the user to the team members and save the team
                team.members.add(user)
                team.save()

                return redirect('/log-in')
            else:
                # Redirect to a login page or handle unauthenticated user as needed
                return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


@login_required
def myaccount(request):
    return render(request, 'myaccount.html')
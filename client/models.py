from django.contrib.auth.models import User
from django.db import models
from team.models import Team

class Client(models.Model):
    team = models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=260)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    
    # sort clients alphabetically
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name



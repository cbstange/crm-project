from django.contrib.auth.models import User
from django.db import models

'''
When a new lead is created, it will be linked to the user
who added it. When a user is deleted, so will all leads 
that the user created. New leads will also show when
they were created. Date & time will also be shown
when an existing lead is modified.
'''
class Lead(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

# Label lead priority. Default is medium.
    CHOICES_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    NEW = 'new'
    CONTACTED = 'contacted'
    GAINED = 'gained'
    LOST = 'lost'

    CHOICES_STATUS = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (GAINED, 'Gained'),
        (LOST, 'Lost'),
    )

# Fields for leads
    name = models.CharField(max_length=260)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NEW)
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
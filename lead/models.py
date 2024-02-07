from django.contrib.auth.models import User
from django.db import models

'''
When a new lead is created, it will be linked to the user
who added it. When a user is deleted, so will all leads 
that the user created. New leads will also show when
they were created.
'''
class Lead(models.Model):
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
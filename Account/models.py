from django.db import models
from django.contrib.auth.models import User

INDUSTRY_CHOICES = [
    ('fianace','Fianace'),
    ('health care', 'Health Care'),
    ('insurance', 'Insurance'),
    ('manufacturing', 'Manufacturing'),
    ('publishing', 'Publishing')
]

class Account(models.Model):
    name = models.CharField(max_length=200,blank=True)
    emai = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    website = models.URLField(max_length=200)
    description = models.TextField()
    assigned_to = models.ManyToManyField(User, related_name='assigner')
    created_on  = models.DateTimeField(auto_now_add=False)
    is_active = models.BooleanField(default=True)


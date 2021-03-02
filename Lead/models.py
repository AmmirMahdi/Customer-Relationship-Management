from django.db import models
from django.contrib.auth.models  import User 



INDUSTRY_CHOICES = [
    ('fianace','Fianace'),
    ('health care', 'Health Care'),
    ('insurance', 'Insurance'),
    ('manufacturing', 'Manufacturing'),
    ('publishing', 'Publishing')
]

class Lead(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField() 
    phone = models.CharField(blank=True)
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    website = models.URLField()
    description = models.TextField() 
    assigned_to = models.ManyToManyField(User)
    created_to  = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
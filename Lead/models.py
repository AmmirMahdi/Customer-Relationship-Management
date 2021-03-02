from django.db import models
from django.contrib.auth.models  import User 



INDUSTRY_CHOICES = [
    ('fianace','Fianace'),
    ('health care', 'Health Care'),
    ('insurance', 'Insurance'),
    ('manufacturing', 'Manufacturing'),
    ('publishing', 'Publishing')
]


LEAD_STATUS = (
    ('assigned', 'Assigned'),
    ('in process', 'In Process'),
    ('converted', 'Converted'),
    ('recycle', 'Recycle'),
    ('dead', 'Dead')
)

LEAD_SOURCE = (
    ('call', 'Call'),
    ('email', 'Email'),
    ('existence', 'Existence'),
    ('partner', 'Partner'),
    ('public', 'Public')
    ('compaign','Compaign')
)

class Lead(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField() 
    phone = models.CharField(blank=True)
    account = ForeignKey(Account, on_delete=mpdels.CASCADE)
    status = models.CharField(max_length=50, choices=LEAD_STATUS)
    source = models.CharField(max_length=50, choices=LEAD_CHOICES)
    address = models.CharField(max_length=50, blank=True)
    website = models.URLField()
    description = models.TextField() 
    assigned_to = models.ManyToManyField(User)
    created_to  = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True, auto_now_add=True)
    is_active = models.BooleanField(default=True)
    enqueryType = models.CharField(max_length=50)


    def __str__(self):
        return self.name, self.email
    
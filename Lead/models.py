from django.db import models
from django.contrib.auth.models  import User 
from Account.models import Account
from django.urls import reverse


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
    ('public', 'Public'),
    ('compaign','Compaign')
)

class Lead(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    email = models.EmailField() 
    phone = models.CharField(max_length=200,blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=LEAD_STATUS)
    source = models.CharField(max_length=50, choices=LEAD_SOURCE)
    address = models.CharField(max_length=50, blank=True)
    website = models.URLField()
    description = models.TextField() 
    assigned_to = models.ManyToManyField(User,max_length=100)
    created_to  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Created')
    created_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    enqueryType = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("lead:detail", kwargs={"pk": self.pk})
    


    def __str__(self):
        return self.name
    
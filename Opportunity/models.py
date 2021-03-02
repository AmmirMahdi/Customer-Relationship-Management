from django.db import models
from Account.models import Account
from django.contrib.auth.models import User 
from Contact.models import Contact


STAGE_CHOICES = (
    ('QUALIFICATION', 'QUALIFICATION'),
    ('NEEDS ANALYSIS', 'NEEDS ANALYSIS'),
    ('VALUE PROPOSITION', 'VALUE PROPOSITION'),
    ('ID.DECISION MAKERS', 'ID.DECISION MAKERS'),
    ('PERCEPTION ANALYSIS', 'PERCEPTION ANALYSIS'),
    ('PROPOSAL/PRICE QUOTE', 'PROPOSAL/PRICE QUOTE'),
    ('NEGOTIATION/REVIEW', 'NEGOTIATION/REVIEW'),
    ('CLOSED WON', 'CLOSED WON'),
    ('CLOSED LOST', 'CLOSED LOST'),
)

class Opportinuty(models.Model):
    name         = models.CharField(max_length=50)
    account      = models.ForeignKey(Account, on_delete=models.CASCADE)
    stage        = models.CharField(max_length=50, choices=STAGE_CHOICES)
    amount       = models.DecimalField(max_digits=12, decimal_places=2)
    lead_souce   = models.CharField(max_length=50)
    probility    = models.CharField(max_length=50)
    contacts     = models.ManyToManyField(Contact)
    closed_by    = models.ForeignKey(User, on_delete=models.CASCADE)
    description  = models.TextField()
    created_by   = models.ForeignKey(User, on_delete=models.CASCADE,related_name='created_by_opportinuty',)
    is_active    = models.BooleanField(default=False)
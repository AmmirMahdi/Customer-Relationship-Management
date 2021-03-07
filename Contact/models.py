from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from Account.models import Account

class Contact(models.Model):
    first_name = models.CharField("First name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)
    account = models.ForeignKey(Account, related_name='lead_account_contacts', on_delete=models.CASCADE, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE,related_name='contact_created_by',)
    createdOn = models.DateTimeField("Created on", auto_now_add=True)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + self.last_name

    def get_absolute_url(self):
        return reverse("contact:detail", kwargs={"pk": self.pk})
    
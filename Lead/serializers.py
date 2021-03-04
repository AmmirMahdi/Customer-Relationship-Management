from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Lead
        fields = ['id', 'name','image','email', 'phone', 'address']
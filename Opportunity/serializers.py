from rest_framework import serializers
from .models import Opportinuty

class OpportinutySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportinuty
        fields = ['name',"account","stage","probility","contacts","closed_by","description","created_by","is_active"]
